"""wikifront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from wiki.models import Wiki_page
from wiki import views
urlpatterns = [
    re_path(r'^$', views.front_page, name='wiki_page_list'), 
    re_path(r'^add/page$', views.add_wiki_page, name='wiki_page_add'),
    re_path(r'^page/(?P<slug>[-\w]+)$', views.wiki_page_details, name='wiki_page_detail'),
    re_path(r'^history/(?P<slug>[-\w]+)$', views.page_history, name='wiki_page_history'),
    re_path(r'^edit/page/(?P<slug>[-\w]+)$', views.edit_wiki_page, name='wiki_page_edit')
]
