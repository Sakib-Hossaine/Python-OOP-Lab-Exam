"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views as myviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home, name='home'),
    path('about/', myviews.about, name='about'),
    path('hospitals/', myviews.hospital_list, name='hospital_list'),
    path('hospital_details/<str:id>', myviews.hospital_details, name='hospital_details'),
    path('upload/', myviews.upload_hospital, name='upload_hospital'),
    path('update/<str:id>', myviews.update_hospital, name='update_hospital'),
    path('delete/<str:id>', myviews.delete_hospital, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

