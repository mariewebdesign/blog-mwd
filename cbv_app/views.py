from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView , DeleteView, UpdateView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy


# Create your views here.

class CBView(View):
    def get(self,request):
        return HttpResponse('Affichage grâce à View')

class AboutView(TemplateView):
    template_name = 'cbv_app/about.html'

    def get_context_data(self,**kwargs):

        # **kwargs : retourne les paramètres de la méthode dans un dictionnaire avec une clé et une valeur
        # *args : retourne les paramètres d ela méthode dans un tuple
        context = super().get_context_data(**kwargs)
        context['data'] = 'Données basiques à afficher'
        return context

class ShopListView(ListView):
    context_object_name = 'shops'
    model = models.Shop

class ShopDetailsView(DetailView):
    model = models.Shop
    context_object_name = 'shop_detail'
    template_name = 'cbv_app/shop_details.html'

    def get_queryset(self):
        return models.Shop.objects.order_by('id')

class ShopCreateView(CreateView):
    fields = ('name','manager','location')
    model = models.Shop

class ShopUpdateView(UpdateView):
    fields = ('name','manager')
    model = models.Shop

class ShopDeleteView(DeleteView):
    model = models.Shop
    success_url = reverse_lazy('cbv_app:shop_list')

