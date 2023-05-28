from elasticsearch import Elasticsearch

from django.http import HttpResponse
from django.shortcuts import render

from .models import Book

# Sửa password lại theo từng server
es = Elasticsearch(
    ["http://localhost:9200/"],
    http_auth=("elastic", "wFhjJdsQdVM66xXuR2yk")
)


# Create your views here.
def index(request):
    """
    Hiển thị tất cả các sách tỏng dataset
    """

    # Thực hiện truy vấn
    search_result = es.search(index="finalproject_index_v3",
                              body={"query": {"match_all": {}}})
    hits = search_result["hits"]["hits"]

    indexContext = {

    }
    return render(request=request,
                  template_name='index.html',
                  context=indexContext)


def detail(request, book):
    """
    Hiện thị thông tin của 1 quyển sách
        và top 20 quyển sách khác có liên quan
    Input: 1 quyển sách
    """
    detailContext = {

    }
    return render(request=request,
                  template_name='detail.html',
                  context=detailContext)


def search(request, keyword):
    """
    Hiển thị danh sách các quyển sách có liên quan đến
        từ khóa được tìm kiếm theo thứ tự
    Input: Từ khóa nhập vào thanh Search
    """
    searchContext = {

    }
    return render(request=request,
                  template_name='index.html',
                  context=searchContext)
