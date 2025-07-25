from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # Keep this for clarity, though its use for media is conditional
from django.views.static import serve # <--- NEW: Import the serve view

admin.site.site_header = "Ray Advertising LLC Control Panel"
admin.site.site_title = "Ray Advertising Admin Portal"
admin.site.index_title = "Welcome to Ray Advertising LLC Control Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls"))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This block is for when DEBUG is True (Django's default static file serving)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)