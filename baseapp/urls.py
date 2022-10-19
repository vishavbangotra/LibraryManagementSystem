from django.contrib import admin
from django.urls import path, include
from .api import get_all_books, get_book_by_id, get_student_detail

urlpatterns = [
    path('', get_all_books),
    path('<int:pk>/', get_book_by_id),
    path('student/<int:pk>/', get_student_detail)
]
