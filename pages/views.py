from django.views.generic import View,TemplateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from books.models import Book,Categoria
from .forms import LibroForm
from django.core.paginator import Paginator

class HomePageView(View):

    def get_queryset(self):
        queryset = Book.objects.filter(cantidad__gte = 1)
        return queryset

    def get_context_data(self, **kwargs):
        context = {}
        book_list = self.get_queryset()
        paginator = Paginator(book_list, 10)  
        page_number = self.request.GET.get('page')  
        page_obj = paginator.get_page(page_number) 
        context['book_list'] = page_obj
        context['form'] = LibroForm()
        return context

    
    def get(self,request,*args, **kwargs):
        return render(request,'home.html',self.get_context_data())

    def post(self,request,*args, **kwargs):
    
        form = LibroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

class error404(TemplateView):
    template_name = '404.html'

