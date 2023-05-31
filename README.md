# IR - DjangoWeb with ElasticSearch

Đồ án cuối kỳ môn Infomation Retrieval

## Elastic Search là gì

Elasticsearch là một công cụ tìm kiếm và phân tích dữ liệu mã nguồn mở được xây dựng trên nền tảng Apache Lucene. Elasticsearch cho phép lưu trữ, tìm kiếm và phân tích các tài liệu có cấu trúc và không cấu trúc với tốc độ rất nhanh và khả năng mở rộng tuyệt vời.

Nó được sử dụng rộng rãi trong các ứng dụng web, trong đó Elasticsearch thường được sử dụng để tìm kiếm và hiển thị các kết quả liên quan cho người dùng. Elasticsearch cũng là một thành phần chính trong hệ sinh thái của Elastic Stack, bao gồm các ứng dụng như Logstash, Kibana và Beats, để thu thập, xử lý và hiển thị dữ liệu log và các thông tin khác từ các hệ thống và ứng dụng.

## Django web là gì

Django là một framework phát triển web được viết bằng Python. Nó cung cấp cho các nhà phát triển một cách tiếp cận khá dễ dàng để phát triển các ứng dụng web phức tạp. Django bao gồm nhiều tính năng, bao gồm ORM (Object-Relational Mapping), hỗ trợ đa ngôn ngữ, hệ thống xử lý URL, xác thực và quản lý phiên và một số thành phần khác giúp việc phát triển ứng dụng web trở nên dễ dàng hơn. Nó cũng có cộng đồng phát triển mã nguồn mở rất lớn và có sẵn nhiều tài liệu và thư viện hỗ trợ cho việc phát triển.

Một số đặc điểm của Django bao gồm:

1. Mô hình MTV: Django xây dựng trên mô hình MTV (Model-Template-View), giúp tách biệt giữa dữ liệu, logic và giao diện người dùng.
2. ORM: Django cung cấp một công cụ ORM (Object-Relational Mapping) để tương tác với cơ sở dữ liệu, giúp các nhà phát triển quản lý dữ liệu dễ dàng hơn.
3. Hỗ trợ đa ngôn ngữ: Django hỗ trợ việc phát triển ứng dụng đa ngôn ngữ.
4. Bảo mật: Django đã tích hợp sẵn các tính năng bảo mật như xác thực, phân quyền và chống CSRF (Cross-site request forgery).
5. Cộng đồng phát triển mã nguồn mở: Django có cộng đồng phát triển lớn, vì vậy rất dễ dàng để tìm kiếm tài liệu và các thư viện hỗ trợ.
6. Tích hợp dễ dàng với các công cụ khác: Django cho phép tích hợp dễ dàng với các công cụ khác như HTML, CSS, JavaScript, jQuery và Bootstrap.

Django là một trong những framework phổ biến nhất trên thế giới và được sử dụng bởi nhiều công ty lớn để phát triển các ứng dụng web.

## Cách tích hợp Elastic search vào Django web

Để tích hợp Elasticsearch vào Django web, có thể sử dụng một số thư viện phổ biến như elasticsearch-dsl và django-elasticsearch-dsl. Các bước cơ bản để tích hợp Elasticsearch vào Django web như sau:

1. Cài đặt *Elasticsearch*: Để sử dụng *Elasticsearch* với Django, trước tiên cần cài đặt Elasticsearch. Elasticsearch có thể được cài đặt trên nhiều hệ điều hành khác nhau và phiên bản mới nhất có thể được tìm thấy trên trang web chính thức của Elasticsearch.
2. Cài đặt *elasticsearch-dsl* và *django-elasticsearch-dsl*: Hai thư viện này cung cấp các lớp xây dựng và công cụ để tương tác với Elasticsearch trong Django.

```bash
pip install elasticsearch-dsl
pip install django-elasticsearch-dsl

```

3. Thiết lập kết nối với Elasticsearch: Trong *[settings.py](http://settings.py/)* của ứng dụng Django, cần thiết lập kết nối với Elasticsearch. Ví dụ:

```python
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
```

4. Định nghĩa các model Elasticsearch: Tạo các lớp Elasticsearch Model với các thuộc tính để mapping với các field trong model của Django.

```python
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Book

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

```

5. Tạo các View và Search: Tạo các view và search queries để tìm kiếm và hiển thị kết quả từ Elasticsearch.

Đó là một số bước cơ bản để tích hợp Elasticsearch vào Django web. Việc tích hợp này sẽ giúp tăng tốc độ tìm kiếm và phân tích dữ liệu của ứng dụng web của bạn.
