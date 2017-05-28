from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from searchapp.models import *
from .models import BPost
from .models import *
from django.http import Http404
# Create your views here.
from django.template import loader

from .search1 import *
from .search1 import BlogPostIndex

# Create your views here.
def index(request):
    context={}
    return render(request,'searchapp/index.html',context)



def search(request):
    result1= request.GET['AY']
    obj=search11(author=result1)
    print('Total %d hits found.' % obj.hits.total)
    total= obj.hits.total
    #keys=list("author","title","text")
    #values=list()
    context={}
    for hit in obj:
            x = BPost(hit.author,hit.title,hit.text)
         #   x.addmethod()
            x.display()
    p=BPost.objects.all()
    
    template=loader.get_template('searchapp/detail.html')    
    return HttpResponse(template.render(context,request))

