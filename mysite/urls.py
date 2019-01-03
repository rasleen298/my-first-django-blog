"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. 
Examples:
Function views
    1.  from my_app import views
    2. To urlpatterns:  path('', views.home, name='home')
Class-based views
    1.  from other_app.views import Home
    2. To urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. The include() function: from django.urls import include, path
    2.To urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
               
