from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'BookWeb_withElasticSearch/Books/template/index.html')

