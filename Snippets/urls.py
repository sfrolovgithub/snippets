"""Snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets_add'),
    #path('snippets/add', views.add_snippet_page_auto_form, name='snippets_add'),
    path('snippets/list', views.snippets_page, name='snippets_list'),
    path('snippets/list/my', views.snippets_page_my, name='snippets_list_my'),
    path('snippets/create', views.snippets_create, name='snippets_create'),
    path('snippets/edit/<int:id>', views.snippets_edit, name='snippets_edit'),
    #path('snippets/create', views.snippets_create_auto_form, name='snippets_create'),
    path('auth/login', views.auth_login, name='auth_login'),
    path('auth/loginout', views.auth_login_out, name='auth_login_out'),
    path('auth/register', views.register, name='register'),
    path('snippets/comment/create', views.snippets_comment_create, name='snippets_comment_create'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

