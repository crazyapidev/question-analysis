#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Feb 19, 2018

@author: 420169
'''

from elasticsearch import Elasticsearch
from elastic_search_db import ES_HOST,ES_PORT

class ElasticDB(object):
    
    class __ElasticDB:
        def __init__(self):
            self.elastic_connection = Elasticsearch(hosts=[{'host': ES_HOST, 'port': int(ES_PORT)}]) 
        def __str__(self):
            return str( self.elastic_connection)
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not ElasticDB.instance:
            ElasticDB.instance = ElasticDB.__ElasticDB()
        return ElasticDB.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)              

