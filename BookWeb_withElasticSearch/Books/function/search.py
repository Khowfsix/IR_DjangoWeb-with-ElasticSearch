from datetime import datetime
from ..models import Book
from ..common import *
import math

def search(query, size):
    global index_name, es
    return es.search(index=index_name,
                     body={
                         "query": query,
                         "from": 0,
                         "size": size,
                         "sort":
                             {
                                 "_score":
                                     {
                                         "order": "desc"
                                     }
                             }
                     })

def getBook_fromResults(search_result, sortype=None):
    listBooks = []

    # Lấy kết quả query sang object Books
    for hit in search_result['hits']['hits']:
        JSbook = hit.get('_source')
        ObBook = Book()
        ObBook.DanhMuc = JSbook.get('Danh mục')
        ObBook.LinkImage = JSbook.get('LinkImage')
        ObBook.Ten = JSbook.get('Tên')
        ObBook.MaSanPham = JSbook.get('Mã sản phẩm')
        ObBook.TacGia = JSbook.get('Tác giả')
        ObBook.DichGia = JSbook.get('Dịch giả')
        ObBook.NhaXuatBan = JSbook.get('Nhà xuất bản')

        if (JSbook.get('Số trang') is not None):
            ObBook.SoTrang = int(JSbook.get('Số trang'))

        ObBook.KichThuoc = JSbook.get('Kích thước')

        if (JSbook.get('Ngày phát hành') is not None):
            ObBook.NgayPhatHanh = datetime.strptime(JSbook.get('Ngày phát hành'), '%d-%m-%Y')

        ObBook.GiaBia = JSbook.get('Giá bìa')
        ObBook.GiaNhaNam = JSbook.get('Giá Nhã Nam')
        ObBook.GioiThieuSach = JSbook.get('Giới thiệu sách')

        # print(ObBook.Ten)
        if ObBook.MaSanPham.strip() != "hết sách":
            listBooks.append(ObBook)
    if sortype is not None and sortype != 'default':
        sortedListBooks = []
        if sortype == 'incName':
            sortedListBooks = sorted(listBooks, key=lambda x: x.Ten)
        elif sortype == 'desName':
            sortedListBooks = sorted(listBooks, key=lambda x: x.Ten, reverse=True)
        elif sortype == 'incPrice':
            sortedListBooks = sorted(listBooks, key=lambda x: x.GiaNhaNam)
        elif sortype == 'desPrice':
            sortedListBooks = sorted(listBooks, key=lambda x: x.GiaNhaNam, reverse=True)
        elif sortype == 'nearDay':
            sortedListBooks = sorted(listBooks, key=lambda x: x.NgayPhatHanh, reverse=True)
        elif sortype == 'farDay':
            sortedListBooks = sorted(listBooks, key=lambda x: x.NgayPhatHanh)
        else:
            # Do nothing
            pass    
        # print(sortedListBooks)
        return sortedListBooks
    
    return listBooks

def searchAll(sortype=None):
    # Truy vấn tất cả dữ liệu trong index bằng match_all()
    ## query all
    query = {
        "match_all": {},
    }
    search_result = search(query, 3000)

    # Lấy kết quả query sang object Books
    return getBook_fromResults(search_result,sortype)

def search_keyword(keyword, sortype=None):
    query = {
        "bool": {
            "should": [
                {
                    "match": {
                        "Danh mục": keyword
                    }
                },
                {
                    "match": {
                        "Tác giả": keyword
                    }
                },
                {
                    "match": {
                        "Tên": keyword
                    }
                },
                {
                    "match": {
                        "Dịch giả": keyword
                    }
                },
                {
                    "match": {
                        "Nhà xuất bản": keyword
                    }
                },
                {
                    "match": {
                        "Giới thiệu sách": keyword
                    }
                }
            ],
            "minimum_should_match": 1
        }
    }
    search_result = search(query, 3000)
    return getBook_fromResults(search_result, sortype=sortype)

def searchOneBook(id,sortype=None):
    queryThisBook = {
        "match": {
            "Mã sản phẩm": id
        }
    }
    print(queryThisBook)
    search_result = search(queryThisBook, 1)
    return getBook_fromResults(search_result=search_result, sortype=sortype)[0]

def searchRelatedBook(myBook,number,sortype=None):
    queryRelatedBook = {
        "bool": {
            "minimum_should_match": 1,
            "should": [
                {
                    "match": {
                        "Danh mục": myBook.DanhMuc
                    }
                },
                {
                    "match": {
                        "Tác giả": myBook.TacGia
                    }
                },
                {
                    "match": {
                        "Tên": myBook.Ten
                    }
                },
                {
                    "match": {
                        "Nhà xuất bản": myBook.NhaXuatBan
                    }
                },
                {
                    "match": {
                        "Giới thiệu sách": myBook.GioiThieuSach
                    }
                }
            ]
            
        }
    }
    search_result = search(queryRelatedBook, number)
    return getBook_fromResults(search_result=search_result, sortype=sortype)[1:]
