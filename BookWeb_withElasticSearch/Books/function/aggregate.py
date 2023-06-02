from ..common import *
def aggregate(aggs):
    global index_name, es
    return es.search(index=index_name,
                    body = {
                        "size": 0,
                        "aggs": aggs
                        }
                    )
def getUniqueCategory():
    """ Lấy danh sách danh mục

    Returns:
        listDanhMuc: kiểu dict chứa key là tên, value là số lượng doc của các danh mục
    """
    aggs = {
                'bucket': {
                'terms': {
                    'field': 'Danh mục.keyword',
                    'size': 10
                    }
                }
            }
    search_result = aggregate(aggs)

    listDanhMuc = {}
    # Lấy kết quả query 
    for bucket in search_result['aggregations']['bucket']['buckets']:
        listDanhMuc[bucket.get('key')] = bucket.get('doc_count')
    return listDanhMuc

def getUniqueAuthor():
    """ Lấy danh sách tác giả

    Returns:
        listTacGia: kiểu dict chứa key là tên tác giả, value là số lượng sách
    """
    aggs = {
                'bucket': {
                'terms': {
                    'field': 'Tác giả.keyword'
                    }
                }
            }
    search_result = aggregate(aggs)

    listTacGia = {}
    # Lấy kết quả query 
    for bucket in search_result['aggregations']['bucket']['buckets']:
        listTacGia[bucket.get('key')] = bucket.get('doc_count')
    return listTacGia

def getUniqueTranslator():
    """ Lấy danh sách dịch giả

    Returns:
        listDichGia: kiểu dict chứa key là tên dịch giả, value là số lượng sách
    """
    aggs = {
                'bucket': {
                'terms': {
                    'field': 'Dịch giả.keyword'
                    }
                }
            }
    search_result = aggregate(aggs)

    listDichGia = {}
    # Lấy kết quả query 
    for bucket in search_result['aggregations']['bucket']['buckets']:
        listDichGia[bucket.get('key')] = bucket.get('doc_count')
    return listDichGia

def getUniquePublisher():
    """ Lấy danh sách nhà xuất bản

    Returns:
        listNXB: kiểu dict chứa key là tên NXB, value là số lượng sách
    """
    aggs = {
                'bucket': {
                'terms': {
                    'field': 'Nhà xuất bản.keyword'
                    }
                }
            }
    search_result = aggregate(aggs)

    listNXB = {}
    # Lấy kết quả query 
    for bucket in search_result['aggregations']['bucket']['buckets']:
        listNXB[bucket.get('key')] = bucket.get('doc_count')
    return listNXB