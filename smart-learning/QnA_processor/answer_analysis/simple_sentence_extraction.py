import spacy
nlp = spacy.load("en_core_web_lg")


prepositions = ["ADP"]
SUBJECT_DEP = ["nsubj", "nsubjpass", "csubj","conj", "csubjpass", "agent", "expl"]
SUBJECT_POS = ["NOUN","PROPN"]
COMPOUNDS = ["compound"]
AUX_VERBS = ["aux","auxpass","pcomp"]
  
def traverse_dep_tree_inorder(fact,root):
 
    if root:
        for token in root.lefts:
            if token.pos_ == "VERB" and token.dep_ != "amod" :
                continue
            traverse_dep_tree_inorder(fact,token)
 
        fact.append(root)
        
        for token in root.rights:
            if token.pos_ == "VERB" and token.dep_ != "amod" :
                continue
            traverse_dep_tree_inorder(fact,token)
            
def form_objects_phrases(negation,objects):
    """
    objects and verbs connected by prepositions
    """
    obj_phrases = []
    for object in objects:
        if object[0].pos_ !="VERB" and object[0].pos_ != "CCONJ":
            obj_phrases.append((" ".join([word.text for word in object]),negation))
    return obj_phrases

def get_subs_from_conjunctions(subs):
    moreSubs = []
    for sub in subs:
        # rights is a generator
        rights = list(sub.rights)
        right_deps = {tok.lower_ for tok in rights}
        if "and" in right_deps or "," in right_deps:
            moreSubs.extend([tok for tok in rights if tok.dep_ in SUBJECT_DEP or tok.pos_ in SUBJECT_POS])
            if len(moreSubs) > 0:
                moreSubs.extend(get_subs_from_conjunctions(moreSubs))
    return moreSubs

def remove_clausal_complement_verb_from_verbs_list(verb,verbs):
    """ 
    open clausal complement (xcomp) of a verb or an adjective is a predicative 
    or clausal complement without its own subject.
    So removing the complement verb
    as this verb no need to form object phrases separately 
    """
    
    for tok in list(verb.lefts) + list(verb.rights):
        if tok.dep_ == "xcomp":
            verbs.remove(tok)
     
def is_negated(tok):
    negations = {"no", "not", "n't", "never", "none"} 
    """ TO DO ADD more negated words """
    for dep in list(tok.lefts) + list(tok.rights):
        if dep.lower_ in negations:
            return True
    return False

def find_subs(tok):
    head = tok.head
    while head.pos_ != "VERB" and head.pos_ not in SUBJECT_POS and head.head != head:
        head = head.head
    if head.pos_ == "VERB":
        subs = [tok for tok in head.lefts if tok.dep_ == "SUB"]
        if len(subs) > 0:
            #verbNegated = isNegated(head)
            subs.extend(get_subs_from_conjunctions(subs))
            return subs #, verbNegated
        elif head.head != head:
            return find_subs(head)
    elif head.dep_ in SUBJECT_DEP:
        return [head] #, isNegated(tok)
    return [] #, False

def get_all_subs(v):
    #verbNegated = isNegated(v)
    subs = [tok for tok in v.lefts if tok.dep_ in SUBJECT_DEP ]
    if len(subs) > 0:
        subs.extend(get_subs_from_conjunctions(subs))
    else:
        foundSubs = find_subs(v)
        subs.extend(foundSubs)
    return subs #, verbNegated

def objs_from_lefts(lefts):
    fact = []
    left_facts = []
    for left in lefts:
        if left.pos_ in prepositions:
            traverse_dep_tree_inorder(fact,left)
            left_facts.append(fact)
            fact = []
    return left_facts
    
def objs_from_rights(rights):
    fact = []
    right_facts = []
    for right in rights:
        traverse_dep_tree_inorder(fact,right)
        right_facts.append(fact)
        fact = []
    return right_facts

def get_all_objs(v):
    objects = objs_from_rights(v.rights)
    objects.extend(objs_from_lefts(v.lefts))
    return objects
    
def generate_sub_compound(sub):
    sub_compunds = []
    for tok in sub.lefts:
        if tok.dep_ in COMPOUNDS:
            sub_compunds.extend(generate_sub_compound(tok))
    sub_compunds.append(sub)
    for tok in sub.rights:
        if tok.dep_ in COMPOUNDS:
            sub_compunds.extend(generate_sub_compound(tok))
    return sub_compunds

def remove_duplicate_sentences(simple_sentences):
    marker = set()
    sentences = [not marker.add(x.casefold()) and x for x in simple_sentences if x.casefold() not in marker]
    return sentences

def extract_simple_sentences(sentence):
    sentence_object = nlp(sentence)
    simple_sentences = []
    verbs = [tok for tok in sentence_object if tok.pos_ == "VERB" and tok.dep_ not in AUX_VERBS]
     
    subjects = []
    for v in verbs:
        subs = get_all_subs(v)
        subjects.extend(subs)
            
    for v in verbs:
        verb_negated = is_negated(v)
        remove_clausal_complement_verb_from_verbs_list(v, verbs)
        objects = get_all_objs(v)
        object_phrases = form_objects_phrases(verb_negated,objects)
        for subject in subjects:
            sub_compound = " ".join([word.text for word in generate_sub_compound(subject)])
            for phrase,negation in object_phrases:
                if negation:
                    verb_text = "not " +  v.text
                else:
                    verb_text = v.text
                simple_sentences.append(sub_compound + " " + verb_text + " " + phrase )
    
    
    return remove_duplicate_sentences(simple_sentences)
           
    

        
