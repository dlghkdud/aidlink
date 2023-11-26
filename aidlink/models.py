from django.db import models

# Create your models here.
class Main(models.Model):
    create_date = models.DateTimeField()

# 행정구역시도시군구
class LOCATIONS(models.Model):
    L1 = models.CharField(max_length=20)
    L2 = models.CharField(max_length=10)

#의료기관기본
class HOSPITAL_BASIC_INFO(models.Model):
    hpid = models.CharField(max_length=10)
    phpid = models.CharField(max_length=10)
    duty_emcls = models.CharField(max_length=4)
    duty_emcls_name = models.CharField(max_length=50)
    duty_addr = models.CharField(max_length=200)
    duty_name = models.CharField(max_length=100)
    duty_tel1 = models.CharField(max_length=14)
    duty_tel3 = models.CharField(max_length=14)
    wgs_84_lon = models.DecimalField(max_digits=17, decimal_places=14)
    wgs_84_lat = models.DecimalField(max_digits=17, decimal_places=14)
    center_type = models.CharField(max_length=1)

#가용병상정보
class AVAILABLE_BED_INFO(models.Model):
    hpid = models.CharField(max_length=10)
    rnum = models.IntegerField()
    phpid = models.CharField(max_length=10)
    hvidate = models.IntegerField()
    hvec = models.IntegerField()
    hvoc = models.IntegerField()
    hvncc = models.IntegerField()
    hvccc = models.IntegerField()
    hvicc = models.IntegerField()
    hvgc = models.IntegerField()
    hvdnm = models.CharField(max_length=3)
    hvctayn = models.CharField(max_length=1)
    hvmrlayn = models.CharField(max_length=1)
    hvangloayn = models.CharField(max_length=1)
    hvventliayn = models.CharField(max_length=1)
    hvamyn = models.CharField(max_length=1)
    hv1 = models.CharField(max_length=14)
    hv2 = models.IntegerField()
    hv3 = models.IntegerField()
    hv4 = models.IntegerField()
    hv5 = models.IntegerField()
    hv6 = models.IntegerField()
    hv7 = models.IntegerField()
    hv8 = models.IntegerField()
    hv9 = models.IntegerField()
    hv10 = models.CharField(max_length=1)
    hv11 = models.CharField(max_length=1)
    hv12 = models.CharField(max_length=14)
    duty_name = models.CharField(max_length=100)
    duty_tel3 = models.CharField(max_length=14)

# 의료기관상세
class HOSPITAL_DETAIL_INFO(models.Model):
    hpid = models.CharField(max_length=10)
    post_cdn1 = models.CharField(max_length=3)
    post_cdn2 = models.CharField(max_length=3)
    hvec = models.IntegerField()
    hvoc = models.IntegerField()
    hvncc = models.IntegerField()
    hvccc = models.IntegerField()
    hvicc = models.IntegerField()
    hvgc = models.IntegerField()
    duty_hayn = models.CharField(max_length=1)
    duty_hano = models.IntegerField()
    duty_inf = models.CharField(max_length=300)
    duty_map_img = models.CharField(max_length=100)
    duty_eryn = models.CharField(max_length=1)
    duty_time_1c = models.CharField(max_length=4)
    duty_time_2c = models.CharField(max_length=4)
    duty_time_3c = models.CharField(max_length=4)
    duty_time_4c = models.CharField(max_length=4)
    duty_time_5c = models.CharField(max_length=4)
    duty_time_6c = models.CharField(max_length=4)
    duty_time_7c = models.CharField(max_length=4)
    duty_time_8c = models.CharField(max_length=4)
    duty_time_1s = models.CharField(max_length=4)
    duty_time_2s = models.CharField(max_length=4)
    duty_time_3s = models.CharField(max_length=4)
    duty_time_4s = models.CharField(max_length=4)
    duty_time_5s = models.CharField(max_length=4)
    duty_time_6s = models.CharField(max_length=4)
    duty_time_7s = models.CharField(max_length=4)
    duty_time_8s = models.CharField(max_length=4)
    mkioskty25 = models.CharField(max_length=1)
    mkioskty1 = models.CharField(max_length=1)
    mkioskty2 = models.CharField(max_length=1)
    mkioskty3 = models.CharField(max_length=1)
    mkioskty4 = models.CharField(max_length=1)
    mkioskty5 = models.CharField(max_length=1)
    mkioskty6 = models.CharField(max_length=1)
    mkioskty7 = models.CharField(max_length=1)
    mkioskty8 = models.CharField(max_length=1)
    mkioskty9 = models.CharField(max_length=1)
    mkioskty10 = models.CharField(max_length=1)
    mkioskty11 = models.CharField(max_length=1)
    dgid_id_name = models.CharField(max_length=50)
    hpbdn = models.IntegerField()
    hpccuyn = models.IntegerField()
    hpcuyn = models.IntegerField()
    hperyn = models.IntegerField()
    hpgryn = models.IntegerField()
    hpicuyn = models.IntegerField()
    hpnicuyn = models.IntegerField()
    npopyn = models.IntegerField()
