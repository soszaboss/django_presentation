from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('books/edit/<int:id>/',login_required( views.edit_book), name='edit_book'),
    path('books/delete/<int:id>/', login_required(views.delete_book), name='delete_book'),
    path('authors/', login_required(views.AuthorsView.as_view()), name='authors'),
    path('authors/edit/<int:id>/',login_required( views.edit_author), name='edit_author'),
    path('authors/delete/<int:id>/', login_required(views.delete_author), name='delete_author'),
     path('create-books/', views.create_books_view, name='create_books'),
]
