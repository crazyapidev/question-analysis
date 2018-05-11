# coding: utf-8

"""
Settings.
"""

NLP_ENGINE =  "google_nlp_api"#"spacy" # "spacy" "nltk"

TOKENIZER = 'WHITE_SPACE_TOKENIZER'

# NLTK config
NLTK_DATA_PATH = ['/home/ubuntu/nltk_data','C:/nltk_data',"D:/nltk_data"]  # List of paths with NLTK data

# Encoding config
DEFAULT_ENCODING = "utf-8"



# CUSTOM ENTITY MODEL PATH 

CUSTOM_ENTITY_MODEL_PATH = r"QnA_processor/data/models/custom_entity_tagger_models/model_crf.pkl"

