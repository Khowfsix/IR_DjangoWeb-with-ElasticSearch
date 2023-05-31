from django.db import models
import json

# Create your models here.
class Book(models.Model):
    DanhMuc = models.TextField(max_length=255)
    # Văn học nước ngoài
    DichGia = models.TextField(blank=True)
    # Lục Hương
    GiaNhaNam = models.IntegerField(blank=True)
    # min = 2400; median = 73600; max = 272000
    GiaBia = models.IntegerField()
    # min = 30000; median = 92000; max = 350000
    GioiThieuSach = models.TextField(blank=True)
    KichThuoc = models.TextField(max_length=255)
    # 14 x 20,5 cm
    LinkImage = models.TextField(blank=True)
    MaSanPham = models.CharField(max_length=255)
    # 8935235219472
    NgayPhatHanh = models.DateField(blank=True)
    # earliest : 03 - 11 - 2009; latest : 19 - 05 - 2023
    NhaXuatBan = models.TextField(max_length=255, blank=True)
    # Hội nhà văn
    SoTrang = models.IntegerField(blank=True)
    # min - 45, median - 340, max - 1600
    TacGia = models.TextField(blank=True)
    # Marc Levy
    Ten = models.TextField()
    # Lòng tốt của bạn cần thêm đôi phần sắc sảo
