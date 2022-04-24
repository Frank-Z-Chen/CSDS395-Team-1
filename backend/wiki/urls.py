from django.urls import path
from . import views


urlpatterns = [
    path('page/', views.type_list),
    path('page/<str:type_name>/', views.page_list),
    path('page/<str:type_name>/<str:page_slug>/', views.page_detail),
    path('ocr/<str:type_name>/<str:page_slug>/', views.OcrView.as_view()),
]