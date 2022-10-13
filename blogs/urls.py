from django.urls import path
from .views import index,blogDetail,searchCategory,search,fileupload,searchWriter
#1 สร้าง เส้นทางก่อน ผ่าน urlpattern
urlpatterns=[
    path('',index),#'' สัญญลักษ์ค่าว่า หมายถึงปล่อยวิ่งตรงไปที่ index ได้เลย
    path('blog/<int:id>',blogDetail,name="blogDetail"),
    path('blog/category/<int:cat_id>',searchCategory,name="searchCategory"),
    path('blog/writer/<str:writer>',searchWriter,name="searchWriter"),
    path('search/',search,name='search'),
    path('blog/category/<int:cat_id>',fileupload,name='fileupload'),
   
]
