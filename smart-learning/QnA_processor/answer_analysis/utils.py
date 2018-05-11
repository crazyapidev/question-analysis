'''
Created on Feb 26, 2018

@author: 574965
'''

get_ner_type_for_answer_type = {
 'ABBR:abb':[''],
 'ABBR:exp':[''],
 'DESC:def':[''],
 'DESC:desc':[''],
 'DESC:manner':[''],
 'DESC:reason':[''],
 'ENTY:animal':['ENTY:ANIMAL'],
 'ENTY:body':['ENTY:BODY'],
 'ENTY:color':['ENTY:COLOR'],
 'ENTY:cremat':['WORK_OF_ART'],
 'ENTY:currency':['MONEY'],
 'ENTY:dismed':[''], # FEAR OF SOMETHING , DISEASES
 'ENTY:event':['EVENT','ENTY:EVENT'],
 'ENTY:food':['ENTY:FOOD'],
 'ENTY:lang':['lANGUAGE'],
 'ENTY:letter':[''], # ALPHABETS
 'ENTY:other':[''],
 'ENTY:product':['PRODUCT','ENTY:PROD'],
 'ENTY:religion':['NORP','ENTY:NORP'],
 'ENTY:sport':['ENTY:SPORT'],
 'ENTY:symbol':[''],
 'ENTY:techmeth':[''], # DESCRIPTION OF OR WAYS OF DOING A PROCESS
 'ENTY:termeq':[''], # ALTERNATE NAMES/TRANSLATIONS OF TERMS
 'ENTY:veh':[''], # NAMES OF SHIPS, AIRCRAFTS, 
 'ENTY:word':[''],
 'ENTY:feeling':['ENTY:FEELING'],
 'ENTY:work_of_art':['ENTY:WORK_OF_ART'],
 'HUM:desc':[''],
 'HUM:gr':['PERSON'],
 'HUM:ind':['PERSON','ENTY:HUM'],
 'HUM:title':[''], # OCCUPATION, POSITION OF SPORT TEAM MEMBERS
 'LOC:GPE':['GPE','ENTY:GPE'],
 'LOC:other':['ENTY:LOC:OTHER','LOC'],
 'NUM:code':[''], # ALPHANUMERIC CODES
 'NUM:count':['CARDINAL','ENTY:CARDINAL'],
 'NUM:date':['DATE','ENTY:DATE'],
 'NUM:dist':[''],
 'NUM:money':['MONEY'],
 'NUM:ord':['ORDINAL','ENTY:ORDINAL'],
 'NUM:other':['CARDINAL'],
 'NUM:perc':['PERCENT'],
 'NUM:period':['ENTY:TIME'], # IT CAN BE TIME IF TIME IS LESS THAN  A DAY IN SPACY
 'NUM:speed':[''],
 'NUM:temp':[''],
 'NUM:volsize':[''],
 'NUM:weight':[''],
 'NUM:quantity':['QUANTITY','ENTY:QUANTITY']}

get_spacy_ner_type_for_answer_type = {
 'ABBR:abb':'',
 'ABBR:exp':'',
 'DESC:def':'',
 'DESC:desc':'',
 'DESC:manner':'',
 'DESC:reason':'',
 'ENTY:animal':'',
 'ENTY:body':'',
 'ENTY:color':'',
 'ENTY:cremat':'WORK_OF_ART',
 'ENTY:currency':'MONEY',
 'ENTY:dismed':'', # FEAR OF SOMETHING , DISEASES
 'ENTY:event':'EVENT',
 'ENTY:food':'PRODUCT',
 'ENTY:instru':'PRODUCT', # NAMES OF INSTRUMENTS
 'ENTY:lang':'lANGUAGE',
 'ENTY:letter':'', # ALPHABETS
 'ENTY:other':'',
 'ENTY:plant':'PRODUCT',
 'ENTY:product':'PRODUCT',
 'ENTY:religion':'NORP',
 'ENTY:sport':'EVENT',
 'ENTY:substance':'PRODUCT', # MATERIALS, CHEMICAL COMPOUNDS
 'ENTY:symbol':'',
 'ENTY:techmeth':'', # DESCRIPTION OF OR WAYS OF DOING A PROCESS
 'ENTY:termeq':'', # ALTERNATE NAMES/TRANSLATIONS OF TERMS
 'ENTY:veh':'', # NAMES OF SHIPS, AIRCRAFTS, 
 'ENTY:word':'',
 'HUM:desc':'',
 'HUM:gr':'PERSON',
 'HUM:ind':'PERSON',
 'HUM:title':'', # OCCUPATION, POSITION OF SPORT TEAM MEMBERS
 'LOC:city':'GPE',
 'LOC:country':'GPE',
 'LOC:mount':'LOC',
 'LOC:other':'GPE',
 'LOC:state':'GPE',
 'NUM:code':'', # ALPHANUMERIC CODES
 'NUM:count':'CARDINAL',
 'NUM:date':'DATE',
 'NUM:dist':'QUANTITY',
 'NUM:money':'MONEY',
 'NUM:ord':'ORDINAL',
 'NUM:other':'CARDINAL',
 'NUM:perc':'PERCENT',
 'NUM:period':'QUANTITY', # IT CAN BE TIME IF TIME IS LESS THAN  A DAY IN SPACY
 'NUM:speed':'QUANTITY',
 'NUM:temp':'QUANTITY',
 'NUM:volsize':'QUANTITY',
 'NUM:weight':'QUANTITY'}

