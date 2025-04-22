from django.urls import path,include
from .views import *

app_name = 'BookLib'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('add_author/', AddAuthor.as_view(), name='add_author'),   
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('delete_author/<int:pk>/', DeleteAuthor.as_view(), name='delete_author'),
    path('update_author/<int:pk>/', UpdateAuthor.as_view(), name='update_author'),
    path('add_book/<int:pk>', AddBook.as_view(), name='add_book'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]
