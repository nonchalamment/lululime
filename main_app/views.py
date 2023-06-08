from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Clothing

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def clothing_index(request):
  closet = Clothing.objects.filter(user=request.user)
  return render(request, 'closet/index.html', { 'closet': closet })

@login_required
def clothing_detail(request, clothing_id):
  clothing = Clothing.objects.get(id=clothing_id)
  return render(request, 'closet/detail.html', { 'clothing': clothing })

class ClothingCreate(LoginRequiredMixin, CreateView):
  model = Clothing
  fields = ['name', 'category', 'msrp']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ClothingUpdate(LoginRequiredMixin, UpdateView):
  model = Clothing
  fields = ['category', 'material', 'msrp']

class ClothingDelete(LoginRequiredMixin, DeleteView):
  model = Clothing
  success_url = '/closet/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('clothing-index')
    else:
      error_message = 'Invalid signup - try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)