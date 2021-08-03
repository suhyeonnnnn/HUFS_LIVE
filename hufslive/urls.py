"""hufslive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',community.views.home, name="home"),
    path('post/<int:post_id>', community.views.detail, name="detail"),
    path('post/new/', community.views.new, name="new"),
    path('post/create/', community.views.create, name="create"),
    path('accounts/', include('allauth.urls')),
    path('new_comment/<int:post_id>', community.views.new_comment, name='new_comment'),
    path('update/<int:post_id>', community.views.update, name='update'),
    path('delete/<int:post_id>', community.views.delete, name='delete'),
]
