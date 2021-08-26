from django.contrib import admin
from django.urls import path
from myapp import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact_us,name="contact"),
    path('about/',views.about,name="about"),
    path('team/',views.team_members,name="team"),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
