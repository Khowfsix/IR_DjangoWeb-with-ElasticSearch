
import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from Books.function import *
from Books.common import *
# Sửa password lại theo từng server

def filter(request):
    """
    Hiển thị danh sách các quyển sách được lọc qua filter
    Input: Filter
    """
    keyword = request.POST.get('keyword')
    print("ccccccccccccc")
    print(keyword)
    # Tạo query
    query, keyword=setQueryByKeyword(keyword,request)
    
    search_result = search(query, 300)
    listBooks = getBook_fromResults(search_result)

    DanhMuc_Selected = getUniqueCategory()
    TacGia_Selected = []
    DichGia_Selected = []
    NhaXuatBan_Selected = []
    gtePageNumber = 10
    ltePageNumber = 1600
    gtePrice = 9600
    ltePrice = 560000
    
    if request.method == 'POST':
        DanhMuc_Selected = request.POST.getlist('DanhMuc')
        TacGia_Selected = request.POST.getlist('TacGia')
        DichGia_Selected = request.POST.getlist('DichGia')
        NhaXuatBan_Selected = request.POST.getlist('NhaXuatBan')
        gtePageNumber = request.POST.get('gtePageNumber')
        if gtePageNumber is None: 
            gtePageNumber = 10
        ltePageNumber = request.POST.get('ltePageNumber')
        if ltePageNumber is None: 
            ltePageNumber = 1600
        gtePrice = request.POST.get('gtePrice')
        if gtePrice is None: 
            gtePrice = 9600
        ltePrice = request.POST.get('ltePrice')
        if ltePrice is None: 
            ltePrice = 560000

    searchContext = {
        "keyword": keyword,
        "Books": listBooks,
        "DanhMucs": getUniqueCategory().keys(),
        "TacGias": getUniqueAuthor().keys(),
        "DichGias": getUniqueTranslator().keys(),
        "NhaXuatBans": getUniquePublisher().keys(),
        'DanhMuc_Selected': DanhMuc_Selected,
        'TacGia_Selected': TacGia_Selected,
        'DichGia_Selected': DichGia_Selected,
        'NhaXuatBan_Selected': NhaXuatBan_Selected,
        'gtePageNumber': gtePageNumber,
        'ltePageNumber': ltePageNumber,
        'gtePrice': gtePrice,
        'ltePrice': ltePrice
    }
    return render(request=request,
                  template_name='index.html',
                  context=searchContext)




# Create your views here.
def index_view(request):
    """
    Hiển thị tất cả các sách trong dataset
    """

    listBooks=searchAll()

    indexContext = {
        "Books": listBooks
    }
    return render(request=request,
                  template_name='index.html',
                  context=indexContext)


def detail_view(request, id):
    """
    Hiện thị thông tin của 1 quyển sách
        và top 20 quyển sách khác có liên quan
    Input: 1 quyển sách
    """

    ## Lấy quyển hiện tại

    thisBook = searchOneBook(id)
    ## Lấy 20 quyển sách co liên quan
    listRelatedBooks = searchRelatedBook(thisBook, 9)

    detailContext = {
        "ThisBook": thisBook,
        "RelatedBooks": listRelatedBooks,
    }

    return render(request=request,
                  template_name='book-detail.html',
                  context=detailContext)

def search_keyword_view(request):
    """
    Hiển thị danh sách các quyển sách có liên quan đến
        từ khóa được tìm kiếm theo thứ tự
    Input: Từ khóa nhập vào thanh Search
    """
    keyword = request.GET.get('keyword')
    if (keyword is None):
        return index_view(request)

    listBooks = []

    # Truy vấn dữ liệu
    listBooks=search_keyword(keyword)

    searchContext = {
        "Books": listBooks
    }
    return render(request=request,
                  template_name='index.html',
                  context=searchContext)
