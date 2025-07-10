from django.shortcuts import render , redirect
from rayMain import settings
from .models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.paginator import Paginator
from math import ceil
# Create your views here.

def send_email(subject_name,recipient_email,message):
    subject = subject_name
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = recipient_email
    mseg=EmailMultiAlternatives( subject, message, email_from, recipient_list )
    mseg.content_subtype="html"
    mseg.send()

def index(request):
    getFeaturedImages=FeaturedIn.objects.all()
    getTrafficImages=TrafficPartners.objects.all()
    getFAQ=FrequentlyAskedQuestions.objects.all()
    getProudly=ProudlySponsoring.objects.all()
    getAllBlog=Blog.objects.all()

    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))

    sendvar={
        'getGalleryImages':getGalleryImages,
        'getFeaturedImages':getFeaturedImages,
        'getTrafficImages':getTrafficImages,
        'getFAQ':getFAQ,
        'getProudly':getProudly,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getAllBlog':getAllBlog
    }
    return render(request,"index.html",sendvar)
def about(request):
    getFeaturedImages=FeaturedIn.objects.all()
    getTrafficImages=TrafficPartners.objects.all()
    getFAQ=FrequentlyAskedQuestions.objects.all()
    getProudly=ProudlySponsoring.objects.all()
    getAllBlog=Blog.objects.all()
    
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
    sendvar={
        'getGalleryImages':getGalleryImages,
        'getFeaturedImages':getFeaturedImages,
        'getTrafficImages':getTrafficImages,
        'getFAQ':getFAQ,
        'getProudly':getProudly,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getAllBlog':getAllBlog
    }
    return render(request,"about.html",sendvar)

def gallery(request):
    getImage=Gallery.objects.all()
    sendvar={
        'getImage':getImage,
    }
    return render(request,"gallery.html",sendvar)

def publisher(request):
    getGalleryImages=Gallery.objects.all()
    getFeaturedImages=FeaturedIn.objects.all()
    getTrafficImages=TrafficPartners.objects.all()
    getFAQ=FrequentlyAskedQuestions.objects.all()
    getProudly=ProudlySponsoring.objects.all()
    getAllBlog=Blog.objects.all()
    
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
    sendvar={
        'getGalleryImages':getGalleryImages,
        'getFeaturedImages':getFeaturedImages,
        'getTrafficImages':getTrafficImages,
        'getFAQ':getFAQ,
        'getProudly':getProudly,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getAllBlog':getAllBlog
    }  
    return render(request,"publisher.html",sendvar)
def advertiser(request):
    getGalleryImages=Gallery.objects.all()
    getFeaturedImages=FeaturedIn.objects.all()
    getTrafficImages=TrafficPartners.objects.all()
    getFAQ=FrequentlyAskedQuestions.objects.all()
    getProudly=ProudlySponsoring.objects.all()
    getAllBlog=Blog.objects.all()
    
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
    sendvar={
        'getGalleryImages':getGalleryImages,
        'getFeaturedImages':getFeaturedImages,
        'getTrafficImages':getTrafficImages,
        'getFAQ':getFAQ,
        'getProudly':getProudly,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getAllBlog':getAllBlog
    }
    return render(request,"advertiser.html",sendvar)

def paypercall(request):
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))

    sendvar={
        'getGalleryImages':getGalleryImages,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
    }
    return render(request,"paypercall.html",sendvar)

def mediabuying(request):
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))

    sendvar={
        'getGalleryImages':getGalleryImages,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
    }
    return render(request,"mediabuying.html",sendvar)

def affiliatenetwork(request):
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))

    sendvar={
        'getGalleryImages':getGalleryImages,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
    }
    return render(request,"affiliatenetwork.html",sendvar)

def leadgeneration(request):
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))

    sendvar={
        'getGalleryImages':getGalleryImages,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
    }
    return render(request,"leadgeneration.html",sendvar)

def blog(request):
    GetAllBlog=Blog.objects.all()
    pagination=Paginator(GetAllBlog,9)
    pageNumber=request.GET.get('page')
    pageObject=pagination.get_page(pageNumber)

    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
    sendvar={
        "GetAllBlog":pageObject,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getGalleryImages':getGalleryImages,
        'totalpage':range(pagination.num_pages+1)
    }
    return render(request,"blog.html",sendvar)

def blogCatagory(request,catagory):
    getcatagory=BlogCategory.objects.get(category=catagory)
    GetAllBlog=Blog.objects.filter(category=getcatagory)
    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
    sendvar={
        "GetAllBlog":GetAllBlog,
        'getcatagory':catagory,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getGalleryImages':getGalleryImages,
    }
    return render(request,"blog.html",sendvar)

def blogSearch(request):
    if request.method=="POST":
        getSearchItem=request.POST.get("searchFild")
        GetAllBlog=Blog.objects.filter(Titel__icontains=getSearchItem)
        getGalleryImages=Gallery.objects.all()
        n=len(getGalleryImages)
        NumberOfSlides=n//4 + ceil((n/4)-(n//4))
        Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
        sendvar={
            "GetAllBlog":GetAllBlog,
            'sliderCunterNumber':range(1,NumberOfSlides),
            'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
            'getGalleryImages':getGalleryImages,
        }
        return render(request,"blog.html",sendvar)
    return  redirect(blog)

def detailBlog(request,id):
    GetAllBlog=Blog.objects.get(id=id)
    sendvar={
        "GetAllBlog":GetAllBlog
    }
    return render(request,"detailBlog.html",sendvar)

def events(request):
    GetAllBlog=Event.objects.all().order_by('-id')
    pagination=Paginator(GetAllBlog,9)
    pageNumber=request.GET.get('page')
    pageObject=pagination.get_page(pageNumber)

    getGalleryImages=Gallery.objects.all()
    n=len(getGalleryImages)
    NumberOfSlides=n//4 + ceil((n/4)-(n//4))
    Mobile_NumberOfSlides=n//2 + ceil((n/2)-(n//2))
    sendvar={
        "GetAllBlog":pageObject,
        'sliderCunterNumber':range(1,NumberOfSlides),
        'Mobile_sliderCunterNumber':range(1,Mobile_NumberOfSlides),
        'getGalleryImages':getGalleryImages,
        'totalpage':range(1,pagination.num_pages+1)
    }
    return render(request,"events.html",sendvar)

def detailevents(request,id):
    GetAllBlog=Event.objects.get(id=id)
    sendvar={
        "GetAllBlog":GetAllBlog
    }
    return render(request,"detailevents.html",sendvar)

def careers(request):
    getalljobs=Career.objects.all()
    if request.method=="POST":
        titel=request.POST.get('jobtitel')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        cv=request.FILES['cv']
        coverlatter=request.POST.get('coverlatter')
        fm=AppliedCandidates(Position=titel,Name=name,Phone=phone,Email=email,CV=cv,Cover_Letter=coverlatter)
        fm.save()

        getcv=AppliedCandidates.objects.filter(Phone=phone)
        if len(getcv) > 1:
            renamecv=AppliedCandidates.objects.filter(Phone=phone)[0].CV
        else:
            renamecv=AppliedCandidates.objects.get(Phone=phone).CV

        Subject=f"{name} applied for {titel} in our company"
        MessageBody=f"<p>{coverlatter}</p><p>{name}</p><p>{phone}</p><p>{email}</p><p><strong>CV Link:</strong>https://www.rayadvertising.com//media/CandidatesCV/{renamecv}</p>"
        recipient_email=["akash.rayadvertising@gmail.com"]
        send_email(Subject,recipient_email,MessageBody)
    sendvar={
        "getalljobs":getalljobs
    }
    return render(request,"careers.html",sendvar)

def careersCatagory(request,catagory):
    getcatagory=CareersCategory.objects.get(category=catagory)
    getalljobs=Career.objects.filter(category=getcatagory)
    sendvar={
        "getalljobs":getalljobs,
        'getcatagory':catagory,
    }
    return render(request,"careers.html",sendvar)

def careersSearch(request):
    if request.method=="POST":
        getSearchItem=request.POST.get("searchFild")
        getalljobs=Career.objects.filter(Titel__icontains=getSearchItem)
        sendvar={
            "getalljobs":getalljobs,
            'True':True
        }
        return render(request,"careers.html",sendvar)
    return  redirect(careers)

def contact(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Phone=request.POST.get("phone")
        Email=request.POST.get("email")
        Message=request.POST.get("message")
        Subject=f"{Name} trying to reach us from the website"
        MessageBody=f"<p><strong>Phone:&nbsp;</strong>{Phone}</p><p><strong>Email:&nbsp;</strong>{Email}</p><p>{Message}</p>"
        recipient_email=["contact@rayadvertising.com"]
        send_email(Subject,recipient_email,MessageBody)
        sendvar={
            'success':'success,'
        }
        return render(request,"contact.html",sendvar)
    return render(request,"contact.html")

def privacypolicy(request):
    getBody=PrivacyPolicy.objects.last()
    sendvar={
        "getBody":getBody
    }
    return render(request,"privacypolicy.html",sendvar)

def TermsandConditions(request):
    getBody=TermsAndConditions.objects.last()
    sendvar={
        "getBody":getBody
    }
    return render(request,"TermsandConditions.html",sendvar)

def disclaimer(request):
    getBody=Disclaimer.objects.last()
    sendvar={
        "getBody":getBody
    }
    return render(request,"disclaimer.html",sendvar)