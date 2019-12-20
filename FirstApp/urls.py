"""FirstApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mainpage.views import home_view, login_view, register_view, logout_view, projects_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view),
    path('home/', home_view),
    path('login/', login_view),
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path('logout/', logout_view),
    path('projects/', projects_view),
    path('', include('django.contrib.auth.urls')),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
