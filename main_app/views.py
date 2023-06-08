from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Clothing

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def clothing_index(request):
  closet = Clothing.objects.all()
  return render(request, 'closet/index.html', { 'closet': closet })

def clothing_detail(request, clothing_id):
  clothing = Clothing.objects.get(id=clothing_id)
  return render(request, 'closet/detail.html', { 'clothing': clothing })

class ClothingCreate(CreateView):
  model = Clothing
  fields = '__all__'

class ClothingUpdate(UpdateView):
  model = Clothing
  fields = ['category', 'material', 'msrp']

class ClothingDelete(DeleteView):
  model = Clothing
  success_url = '/closet/'