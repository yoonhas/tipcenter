"""TipCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from PSS import views as PSS_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^PSS/', include('PSS.urls')),
    url(r'^$', PSS_views.IndexView.as_view(), name='root'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup$',PSS_views.CreateUserView.as_view(), name='signup'),
    url(r'^accounts/signup/done$',PSS_views.RegisteredView.as_view(), name='create_user_done'),
]