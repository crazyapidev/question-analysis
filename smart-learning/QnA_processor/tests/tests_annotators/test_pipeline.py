try:
    from unittest import mock
except ImportError:
    import mock

from unittest import TestCase

from QnA_processor.annotators.pipeline import AnnotatorPipeline

class TestPipeline(TestCase):

#     def patch_object(self, *args, **kwargs):
#         patcher = mock.patch.object(*args, **kwargs)
#         patched = patcher.start()
#         patched.patcher = patcher
#         self.addCleanup(patcher.stop)
#         return patched

    def test_applies_all_annotators_to_the_given_doc(self):
        annotator1 = mock.MagicMock()
        annotator1.side_effect = lambda x: x.call_order.append(1)
        annotator2 = mock.MagicMock()
        annotator2.side_effect = lambda x: x.call_order.append(2)

        doc = mock.MagicMock()
        doc.call_order = []
        p = AnnotatorPipeline([annotator1, annotator2])
        p.process(doc)
        annotator1.assert_called_once_with(doc)
        annotator2.assert_called_once_with(doc)
        self.assertEqual(doc.call_order, [1, 2])
