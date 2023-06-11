
import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Book
from Books.function import *
from Books.common import *
from django.core.cache import caches

def autocompleSearch(request):
    if request.method == "GET":
        word = request.GET.get('keyword').lower()
        print("keyyyyyyyyy")
        print(word)
        query = {
            "multi_match": {

      "query": word,

      "type": "bool_prefix",
      
      "operator": "or",

      "fields": [

        "Tên.search_as_you_type",

        "Tên.search_as_you_type._2gram",

        "Tên.search_as_you_type._3gram"
      ]

    }
        }
        
        listBooks = []
        search_result = search(query, 5)
        # Lấy kết quả query sang object Books
        for hit in search_result['hits']['hits']:
            JSbook = hit.get('_source')
            JSbook.get('Tên')
            # print(ObBook.Ten)
            if JSbook.get('Mã sản phẩm').strip() != "hết sách":
                listBooks.append(JSbook.get('Tên'))
        print('KQTK')
        print(listBooks)
        return JsonResponse({'books': listBooks})
    return render(request=request, template_name="index.html")


def filter(request):
    """
    Hiển thị danh sách các quyển sách được lọc qua filter
    Input: Filter
    """
    global MYQUERY, MYKEYWORD
    keyword = request.POST.get('keyword')
    DanhMuc_Selected = []
    TacGia_Selected = []
    DichGia_Selected = []
    NhaXuatBan_Selected = []
    gtePageNumber = 10
    ltePageNumber = 1600
    gtePrice = 9600
    ltePrice = 560000
    gteReleaseDate = None
    lteReleaseDate = None
    sortype = request.POST.get('sort-type')
    print(sortype)
    # Tạo query
    # query, keyword=setQueryByKeyword(keyword,request)
    if request.GET.get('page') is None or MYQUERY is None:
        MYQUERY, MYKEYWORD=setQueryByKeyword(keyword,request)
    
    search_result = search(MYQUERY, 300)
    listBooks = getBook_fromResults(search_result, sortype=sortype)

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
        gteReleaseDate = request.POST.get('gteReleaseDate')
        lteReleaseDate = request.POST.get('lteReleaseDate')

    if MYKEYWORD is not None and MYKEYWORD!='':
        header=f"Kết quả tìm kiếm cho '{MYKEYWORD}': {len(listBooks)}"
    elif request.method == 'POST':
        header=f"Kết quả lọc: {len(listBooks)}"
    else:
        header='300 quyển sách đầu tiên'

    searchContext = paging(request, {
        'Header':header,
        "keyword": MYKEYWORD,
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
        'ltePrice': ltePrice,
        'gteReleaseDate': gteReleaseDate,
        'lteReleaseDate': lteReleaseDate,
        'sort': sortype,
    })
    return render(request=request,
                  template_name='index.html',
                  context=searchContext)




# Create your views here.
def index_view(request):
    """
    Hiển thị tất cả các sách trong dataset
    """

    listBooks=searchAll()

    temp={
        'Header':'300 quyển sách đầu tiên',
        "Books": listBooks,
    }
    indexContext = paging(request,temp)
    
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

    searchContext = paging(request,{
        'Header':f"Kết quả tìm kiếm cho '{keyword}': {len(listBooks)}",
        "Books": listBooks,
    })
    return render(request=request,
                  template_name='index.html',
                  context=searchContext)

def paging(request,preView):
    try:
        page=request.GET.get('page')
    except:
        pass
    if page is None:
        page=1
    else:
        page=int(page)

    preView['Pages']=list(range(1,math.ceil(len(preView['Books'])/BPP)+1))
    preView['Page']=page
    preView['Books']=preView['Books'][(page-1)*BPP:page*BPP]
    return preView