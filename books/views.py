from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import View
from django.views.generic import ListView,DetailView,View
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.shortcuts import render
from .models import Book,Categoria,Review,likes,bookview,Reserva
from .forms import formcomentarios

class BookListView(ListView):
    model = Book
    paginate_by = 10
    context_object_name = "book_list"
    template_name = "books/book_list.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(cantidad__gte = 1)
        return queryset


class BookDetailView(View):
    template_name = "books/book_detail.html"

    def get_object(self, queryset=None): 
        try:
            instance = Book.objects.get(id=self.kwargs['pk'])
        except:
            pass
        return instance

    def get_context_data(self, **kwargs):
        context = {}
        
        context['listacomentarios'] = Review.objects.select_related().filter(book=self.kwargs['pk'])
        context['book']=get_object_or_404(Book,pk=self.kwargs['pk'])
        context['form']=formcomentarios()
        return context


   
    def get(self,request,pk,*args, **kwargs):
        book=get_object_or_404(Book,pk=self.kwargs['pk'])
        if self.get_object().cantidad > 0: 
            if request.user.is_authenticated: 
                bookview.objects.get_or_create(usuariovistas=request.user,book=book)
            return render(request,self.template_name,self.get_context_data())
        return redirect('book_list')

    def post(self,request,pk,*args, **kwargs):
        form=formcomentarios()
        if request.method =='POST':
            form = formcomentarios(request.POST) 
            if form.is_valid():
                post = get_object_or_404(Book,pk=pk)
                form.author = request.user
                comentario = form.cleaned_data.get('review')
                p,created = Review.objects.get_or_create(author=form.author,book=post,review=comentario)
                p.save()
                return redirect('book_list')

class SearchResultsListView(ListView): 
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    def get_queryset(self): 
        query = self.request.GET.get("q")
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


class Book_category(View):
    def get(self,request,slug,*args, **kwargs):
        category_list = Book.objects.filter(categoria=Categoria.objects.get(slug=slug))
        con = {
            'list_category':category_list,
        }
        return render(request,'books/book_category.html',con)



class libros_reservados(LoginRequiredMixin,ListView):
    model = Reserva 
    context_object_name = "book_reservados_list"
    template_name = "books/libros_reservados.html"
    login_url = "account_login" 
    
    def get_queryset(self):
        queryset = self.model.objects.filter(estado = True,usuario = self.request.user)
        return queryset
#-----------------------------------------------------------likes y vistas-------------------------------------------
def like(request,pk):
    if request.user.is_authenticated:
        book = get_object_or_404(Book,pk=pk)
        like_qs = likes.objects.filter(user=request.user,book=book)
        if like_qs.exists():
            like_qs[0].delete()
            return redirect('book_list')
        likes.objects.create(user=request.user,book=book)
        return redirect('book_list')
    return redirect('account_login')



def reservarlibro(request,pk):
    if request.user.is_authenticated:
        reservalibro = get_object_or_404(Book,pk=pk)
        Reserva.objects.create(
            usuario = request.user,
            libro=get_object_or_404(Book,pk=pk)
        )
    return redirect('libros_reservados')


