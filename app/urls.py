from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name="home"),
    path('about-us', about, name="about"),
    path('publisher', publisher, name="publisher"),
    path('advertiser', advertiser, name="advertiser"),
    path('paypercall', paypercall, name="paypercall"),
    path('mediabuying', mediabuying, name="mediabuying"),
    path('affiliatenetwork', affiliatenetwork, name="affiliatenetwork"),
    path('leadgeneration', leadgeneration, name="leadgeneration"),
    path('blog', blog, name="blog"),
    path('blog/q/', blogSearch, name="blogSearch"),
    path('blog/q/<str:catagory>', blogCatagory, name="blogcatagory"),
    path('blog/page/<int:id>', detailBlog, name="detailBlog"),
    path('events', events, name="events"),
    path('gallery', gallery, name="gallery"),
    path('events/page/<int:id>', detailevents, name="detailevents"),
    path('careers', careers, name="careers"),
    path('careers/q/<str:catagory>', careersCatagory, name="careerscatagory"),
    path('careers/q/', careersSearch, name="careersSearch"),
    path('contact', contact, name="contact"),
    path('privacypolicy', privacypolicy, name="privacypolicy"),
    path('termsandconditions', TermsandConditions, name="TermsandConditions"),
    path('disclaimer', disclaimer, name="disclaimer"),
]
