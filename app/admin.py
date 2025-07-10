from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Gallery)
admin.site.register(TrafficPartners)
admin.site.register(FeaturedIn)
admin.site.register(FrequentlyAskedQuestions),
admin.site.register(ProudlySponsoring),
admin.site.register(CareersCategory),



class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
admin.site.register(BlogCategory,BlogCategoryAdmin),

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
admin.site.register(EventCategory,EventCategoryAdmin),

class EventsAdmin(admin.ModelAdmin):
    list_display = ('Titel','category',)
    search_fields = ('Titel','category',)
admin.site.register(Event,EventsAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('Titel','category',)
    search_fields = ('Titel','category',)
admin.site.register(Blog,BlogAdmin)

class CareersAdmin(admin.ModelAdmin):
    list_display = ('Titel','vacancy','Experience','Experience','category')
    search_fields = ('Titel',)
admin.site.register(Career,CareersAdmin)

class AppliedCandidatesAdmin(admin.ModelAdmin):
    list_display = ('Position','Name','Phone','CV',)
    search_fields = ('Position','Name','Phone',)
admin.site.register(AppliedCandidates,AppliedCandidatesAdmin)

class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('Last_Update',)
admin.site.register(PrivacyPolicy,PrivacyPolicyAdmin)

class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('Last_Update',)
admin.site.register(TermsAndConditions,TermsAndConditionsAdmin)

class DisclaimerAdmin(admin.ModelAdmin):
    list_display = ('Last_Update',)
admin.site.register(Disclaimer,DisclaimerAdmin)
