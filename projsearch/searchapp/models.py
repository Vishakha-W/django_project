from django.db import models

# Create your models here.
from django.db import models
from elasticsearch import Elasticsearch
# Create your models here.
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date,Search,Q
from elasticsearch import Elasticsearch
connections.create_connection()

class BPost(models.Model):
          author = models.CharField(max_length=200)
          title = models.CharField(max_length=200)
          text = models.TextField(max_length=1000)
                
          def display(self):
              print(" ------->"+self.author+self.title+self.text )            
          def __str__(self):
             return '%s %s %s' % (self.author, self.title,self.text)
            

def search11(author):
    s = Search()
    print("Author you searching for"+author)
    s=s.query('match',AY=author)
    response = s.execute()
   #  print('Total %d hits found.' % response.hits.total)
   # total= response.hits.total
   # for count in range(total):
     #   x = BPost()
      #  for hit in s:
      #      #a=BPost(hit.author,hit.title,hit.text)
       #     print("hellooo--> "+hit.title)
      #      print("author-->"+hit.author)
     #       print("text"+hit.text)
    #        x.addmethod(hit.author,hit.title,hit.text)
    return response

