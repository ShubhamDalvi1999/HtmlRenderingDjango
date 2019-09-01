from django.http import *
from django.views.decorators.csrf import *

data={
    'name':'shubham'
}
def hello(req):
    return HttpResponse('Hello world!')

def getdata(req):
    return JsonResponse(data)

@csrf_exempt
def postdata(req):
    print(req.POST.dict())
    data.update(req.POST.dict())
    return JsonResponse(data)

def renderhtml(req):
    content='''
    <h1>hi django <h1>
    <h2>HI !<h2>
    '''
    return HtmlResponse(content,content_type='text/html')#html response 