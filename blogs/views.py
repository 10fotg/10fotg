
from email.mime import image
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from category.models import Category
from .models import Blogs

from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger


# Create your views here.แสดงบทความที่จะโชว์
def index(request):
    categories = Category.objects.all().order_by('-pk')#ดึงมาจาก apps/models.py category โดยเขียนฟังชั่น categories ทั้งหมด ตามด้วยการนำเอา category มาใช้ทีละอัน
    blogs=Blogs.objects.all().order_by('-pk')
    latest = Blogs.objects.all().order_by('-pk')[:3]
    second = Blogs.objects.all().order_by('name')[:3]
    last = Blogs.objects.all().order_by('views')[:3]
    

    #บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    #บทความแนะนำ
    suggestion = Blogs.objects.all().order_by('views')[:3]
    
  
    #pagination แสดงบทความทั้งหมด #ดึงมาแสดงบทความหน้าแรก
    paginator = Paginator(blogs,9)
    try:
        page = int(request.GET.get('page','1'))
    except :
        page = 1
    
    try :
        blogPerpage = paginator.page(page)
    except (EmptyPage,PageNotAnInteger):
        blogPerpage = paginator.page(paginator.num_pages)

    return render(request,"frontend/index.html",{'fileupload':fileupload,'categories':categories,'blogs':blogPerpage,'latest':latest,'popular':popular,'suggestion':suggestion,'second':second,'last':last,})

def blogDetail(request,id):
    categories = Category.objects.all()
    #บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    #บทความแนะนำ
    suggestion = Blogs.objects.all().order_by('views')[:3]

    singleBlog = Blogs.objects.get(id=id)
    singleBlog.views = singleBlog.views+1
    singleBlog.save()
    return render(request,"frontend/blogDetail.html",{"blog":singleBlog,'categories':categories,'popular':popular,'suggestion':suggestion})

def searchCategory(request,cat_id):
    blogs = Blogs.objects.filter(category_id=cat_id)
    #บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]
    #บทความแนะนำ
    suggestion = Blogs.objects.all().order_by('views')[:3]
    categoryName = Category.objects.get(id=cat_id)
    categories = Category.objects.all()
    return render(request,"frontend/searchCategory.html",{"blogs":blogs,'categories':categories,'popular':popular,'suggestion':suggestion,"categoryName":categoryName})

def searchWriter(request,writer):
    blogs = Blogs.objects.filter(writer = writer) 
    categories = Category.objects.all()
    suggestion = Blogs.objects.all().order_by('views')[:3]
    popular = Blogs.objects.all().order_by('-views')[:3]
    return render(request,"frontend/searchWriter.html",{"blogs":blogs,'categories':categories,'popular':popular,'suggestion':suggestion,"writer":writer})

def search(request):
    blogs = Blogs.objects.filter(name__contains=request.GET['title'])
    return render(request,'frontend/index.html',{'blogs':blogs})



def fileupload(request):
    
        
    fileupload = Blogs.objects.filter()
    return render(request,"frontend/index.html",{'fileupload':fileupload,})




    
    
   
   

        


