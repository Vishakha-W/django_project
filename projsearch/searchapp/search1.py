from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date,Search,Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from searchapp.models import *
#from myapp.models import BPost
connections.create_connection()

#client = Elasticsearch()


class BlogPostIndex(object):
          author = Text()
          title = Text()
          text = Text()
          instances = []

##          def __init__(self,author,title,text):
#              self.author = author
#              self.title = title
#              self.text = text
#              BlogPostIndex.instances.append(self)


     #     def get_instances():
     #         return list(BlogPostIndex.instances)

            
#def search11(author):
#    s = Search()
#    print(author)
#    s=s.query('match',author=author)   
#    response = s.execute()
#    print('Total %d hits found.' % response.hits.total)
#    total= response.hits.total
#    for count in range(total):
#        for hit in s:
#            a=BlogPostIndex(author=hit.author,title=hit.title,text=hit.text)
#            print("hellooo--> "+hit.title)
#            print("author-->"+hit.author)
#            print("text"+hit.text)
#    return response

