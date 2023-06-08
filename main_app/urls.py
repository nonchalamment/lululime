from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('closet/', views.clothing_index, name='clothing-index'),
  path('closet/<int:clothing_id>/', views.clothing_detail, name='clothing-detail'),
  path('closet/create/', views.ClothingCreate.as_view(), name='clothing-create'),
  path('closet/<int:pk>/update/', views.ClothingUpdate.as_view(), name='clothing-update'),
  path('closet/<int:pk>/delete/', views.ClothingDelete.as_view(), name='clothing-delete'),
]