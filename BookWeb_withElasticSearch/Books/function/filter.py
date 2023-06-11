import datetime
from dateutil.parser import parse

def setQueryByKeyword(keyword,request):
    if keyword is None or keyword=='':
        keyword = ''
        query = {
            "bool": {
                "must": [
                    {
                        "bool": {
                        "should": categoryFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": authorFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": translatorFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": publisherFilter(request)
                        }
                    }
                ],
                "filter": [
                    {
                        "range": {
                            "Giá Nhã Nam": priceFilter(request=request)
                        }
                    },
                    {
                        "range": {
                            "Ngày phát hành": releaseDateFilter(request)
                        }
                    },
                    {
                        "range": {
                            "Số trang": pageNumberFilter(request)
                        }
                    }
                ]
            }
        }
    else:
        print('co key')
        query = {
            "bool": {
                "must": [
                    {
                        "bool": {
                        "should": categoryFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": authorFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": translatorFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": publisherFilter(request)
                        }
                    },
                    {
                        "bool": {
                            "should": {
                                "multi_match" : {
                                "query":    keyword, 
                                "fields": [ "Giới thiệu sách", "Tên^5", "Tác giả^2" ] 
                                }
                            },
                        }
                    }
                ],
                "filter": [
                    {
                        "range": {
                            "Giá Nhã Nam": priceFilter(request=request)
                        }
                    },
                    {
                        "range": {
                            "Ngày phát hành": releaseDateFilter(request)
                        }
                    },
                    {
                        "range": {
                            "Số trang": pageNumberFilter(request)
                        }
                    }
                ]
            }
        }
    return query, keyword

def priceFilter(request):
    """
    Hiển thị tất cả các sách trong khoảng giá được nhập vào 
    Input: Request 
    Output: Query thành phần trong phần range trong query tổng
    """
    # Lấy giá trị giá nhỏ nhất được nhập từ web
    gtePrice = request.POST.get('gtePrice')
    # Lấy giá trị giá lớn nhất được nhập từ web
    ltePrice = request.POST.get('ltePrice')
    # Nếu không có giá trị trong 2 biến đó 
    if gtePrice is None and ltePrice is None:
        # Thì trả về rỗng --> tìm trên tất cả khoảng giá
        return {}
    else:
        return {
            "gte": gtePrice,
            "lte": ltePrice
            }

def pageNumberFilter(request):
    """
    Hiển thị tất cả các sách trong khoảng số trang được nhập vào 
    Input: Request 
    Output: Query thành phần trong phần range trong query tổng
    """
    # Lấy giá trị số trang nhỏ nhất được nhập từ web
    gtePageNumber = request.POST.get('gtePageNumber')
    # Lấy giá trị số trang lớn nhất được nhập từ web
    ltePageNumber = request.POST.get('ltePageNumber')
    # Nếu không có giá trị trong 2 biến đó 
    if gtePageNumber is None and ltePageNumber is None:
        # Thì trả về rỗng --> tìm trên tất cả khoảng số trang
        return {}
    else:
        return {
            "gte": gtePageNumber,
            "lte": ltePageNumber
            }

def releaseDateFilter(request):
    """
    Hiển thị tất cả các sách trong khoảng ngày phát hành được nhập vào 
    Input: Request 
    Output: Query thành phần trong phần range trong query tổng
    """
    gteReleaseDate = request.POST.get('gteReleaseDate')
    lteReleaseDate = request.POST.get('lteReleaseDate')
    # Nếu không có giá trị 1 trong 2 biến đó 
    if gteReleaseDate is None or lteReleaseDate is None or len(gteReleaseDate) != 10 or len(gteReleaseDate) != 10:
        # Thì trả về rỗng --> tìm trên tất cả khoảng ngày phát hành
        return {}   
    # Lấy giá trị ngày phát hành nhỏ nhất được nhập từ web
    gteReleaseDate = parse(gteReleaseDate).date().strftime("%d-%m-%Y")
    # Lấy giá trị ngày phát hành lớn nhất được nhập từ web
    lteReleaseDate = parse(lteReleaseDate).date().strftime("%d-%m-%Y")
    
    return {
        "gte": gteReleaseDate,
        "lte": lteReleaseDate
        }

def categoryFilter(request):
    """
    Hiển thị tất cả các sách trong các danh mục được chọn 
    Input: Request 
    Output: Query thành phần trong query tổng
    """
    DanhMuc = []
    if request.method == 'POST':
        DanhMuc = request.POST.getlist('DanhMuc')
    
    if DanhMuc == []:
        return [];
    
    query = []
    for loai in DanhMuc:
        query.append({"match_phrase": {"Danh mục": loai}})
    return query

def authorFilter(request):
    """
    Hiển thị tất cả các sách trong các tác giả được chọn 
    Input: Request 
    Output: Query thành phần trong query tổng
    """
    TacGia = []
    if request.method == 'POST':
        TacGia = request.POST.getlist('TacGia')
    
    if TacGia == []:
        return [];
    
    query = []
    for tacgia in TacGia:
        query.append({"match_phrase": {"Tác giả": tacgia}})
    return query

def translatorFilter(request):
    """
    Hiển thị tất cả các sách trong các tác giả được chọn 
    Input: Request 
    Output: Query thành phần trong query tổng
    """
    DichGia = []
    if request.method == 'POST':
        DichGia = request.POST.getlist('DichGia')
    
    if DichGia == []:
        return [];
    
    query = []
    for dichgia in DichGia:
        query.append({"match_phrase": {"Dịch giả": dichgia}})
    return query

def publisherFilter(request):
    """
    Hiển thị tất cả các sách trong các nhà xuất bản được chọn 
    Input: Request 
    Output: Query thành phần trong query tổng
    """
    NXB = []
    if request.method == 'POST':
        NXB = request.POST.getlist('NhaXuatBan')
    
    if NXB == []:
        return [];
    
    query = []
    for nxb in NXB:
        query.append({"match_phrase": {"Nhà xuất bản": nxb}})
    return query