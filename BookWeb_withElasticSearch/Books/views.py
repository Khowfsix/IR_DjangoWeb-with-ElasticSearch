from django.shortcuts import render
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'BookWeb_withElasticSearch/Books/template/index.html')


@registry.register_document
class BookDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'books'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Book # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'author',
            'description',
        ]