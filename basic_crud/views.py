from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AuthorsForm, BooksForm
from .models import Authors, Books
from django.core.paginator import Paginator


# Function Based View
def index(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    books = Books.objects.all().order_by('-id')
    form = BooksForm()
    books_and_form_update = [
        {
            'book': book,
            'form': BooksForm(instance=book)
        } for book in books
    ]

    # Ici django vous gere la logique de la pagination en peu de ligne
    # ce qui peut vous etre utile par exemple lors d'un conception de site e-commerce 
    # et que vous avez besoin de 10 articles par page etc
    #  
    paginator = Paginator(books_and_form_update, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    #####################################

    context = {
        'books': page,
        'form': form
    }
    return render(request, 'main/index.html', context)

# Class Based View
class AuthorsView(View):
    form_class = AuthorsForm
    template_name = 'main/author.html'
    paginate_by = 5
    model = Authors

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            """
                Permes d'enregistrer les informations de l'auteur sans pour autant 
                gerer la logique de l'enregistrement, ce qui ne veut pas dire que vous ne pouvez pas le faire manuellement
            
            """
            form.save(commit=True)
            return redirect('authors')

    def get(self, request, *args, **kwargs):
        authors = Authors.objects.all().order_by('-id')
        form = self.form_class()
        authors_and_form_update = [
            {
                'author': { 'id': author.id, 'fullname': author.fullname, 'birth_date': author.birth_date, 'nationality': author.nationality},
                'form': self.form_class(instance=author)
            } for author in authors
        ]


        paginator = Paginator(authors_and_form_update, self.paginate_by)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context = {
            'authors': page,
            'form': form
        }
        print(context)
        return render(request, self.template_name, context)

#######################################################################################################################################################""
def edit_author(request, id):
    author = get_object_or_404(Authors, id=id)
    if request.method == "POST":
        """
            Permet d'editer les informations de l'auteur et
            charger les informotions de l'auteur dans le formulaire
            de modification automatique sans que ayez à gerer la logique vous meme ni avec du script   
        """
        form = AuthorsForm(request.POST, instance=author)
        if form.is_valid():
            author.fullname = form.cleaned_data['fullname']
            author.birth_date = form.cleaned_data['birth_date']
            author.nationality = form.cleaned_data['nationality']
            author.save()
            return redirect('authors')
    else:
        form = AuthorsForm(instance=author)
    return render(request, 'main/edit_author.html', {'form': form})

def delete_author(request, id):
    author = get_object_or_404(Authors, id=id)
    author.delete()
    return redirect('authors')

def edit_book(request, id):
    book = get_object_or_404(Books, id=id)
    if request.method == "POST":
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.isbn = form.cleaned_data['isbn']
            book.publication_date = form.cleaned_data['publication_date']
            book.author = form.cleaned_data['author']
            book.save()
            return redirect('index')
    else:
        form = BooksForm(instance=book)
    return render(request, 'main/edit_book.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return redirect('index')