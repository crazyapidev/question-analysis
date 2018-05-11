
from elastic_search_db.elastic_search_dsl import ElasticDB
from elastic_search_db import ES_HOST,ES_PORT,INDEX,TYPE
import requests

class FetchFromES(object):
    
    def __init__(self):
        self.es = ElasticDB()
        self.check_es_connection()
        self.check_index_exists()
        
    def check_es_connection(self):
         
        connection_url = 'http://{}:{}'.format(ES_HOST,ES_PORT)
        status = requests.get(connection_url)
        
    def check_index_exists(self):
        try :
            self.es.elastic_connection.indices.exists(index=INDEX)
        except:
            raise Exception("No Index found with name {}".format(INDEX))
        
    def fetch_lesson_content_from_es(self,lesson_name):
        results = self.es.elastic_connection.search(index=INDEX, doc_type="books", body=  { 
                    "query" : {
                      "match" : {
                        "books.book_name": "Seasons and Weather "
                        }
                    }
                })
        if results["hits"]["hits"]:
            return results["hits"]["hits"][0]["_source"]
        else:
            None
            
    def fetch_assessment_qna_from_es(self,lesson_name):
        results = self.es.elastic_connection.search(index=INDEX, doc_type="assessment", body= {
                      "query": {
                        "match": {
                            "lesson_name" : "What's the weather like"
                        }
                      }
                    })
        if results["hits"]["hits"]:
            if results["hits"]["hits"][0]["_source"]["lesson_name"].strip().lower() == lesson_name.strip().lower():
                return results["hits"]["hits"][0]["_source"]["questions"]
        else:
            None
            
    def fetch_document_from_es(self,query):
        paragraphs = []
        results = self.es.elastic_connection.search(index=INDEX, doc_type="paragraph", body= {
                      "query": {
                        "match": {
                          "paragraph": {
                            "query":query,
                            "minimum_should_match": "70%" 
                            
                          }
                        }
                      }
                    }
                )
        if results["hits"]["hits"]:
            for item in results["hits"]["hits"]:
                paragraphs.append(item["_source"]["paragraph"])
            return paragraphs
        else:
            None

            
    
    