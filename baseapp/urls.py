from django.contrib import admin
from django.urls import path, include
from .api import get_all_books, get_book_by_id, get_student_detail, search_book_by_name, get_all_students

urlpatterns = [
    path('', get_all_books),
    path('<int:pk>/', get_book_by_id),
    path('books/<str:param_name>', search_book_by_name),
    path('students/', get_all_students),
    path('students/<int:pk>/', get_student_detail)
]
