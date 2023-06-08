from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Clothing

closet = [
  Clothing('Energy Bra', 'Sports Bra', 'Luxtreme', 68),
  Clothing('Align Pant HR 25in', 'Leggings', "Nulu", 98),
  Clothing('Invigorate HR Short 10in', 'Shorts', "Everlux", 68),
  Clothing('Court Rival HR Skirt', 'Skirt', "Swift", 68)
]

# Create your views here.
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