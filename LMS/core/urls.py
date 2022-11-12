from django.contrib import admin
from django.urls import path, include
from .views import get_all_books, get_book_by_id, get_student_detail, search_book_by_name, get_all_students, get_books_by_category, issue_book_by_student

urlpatterns = [
    path('books/', get_all_books),
    path('books/id/<int:pk>/', get_book_by_id),
    path('books/name/<str:param_name>', search_book_by_name),
    path('books/category/<str:param_name>', get_books_by_category),
    path('students/', get_all_students),
    path('students/<int:pk>/', get_student_detail),
    path('books/issue/', issue_book_by_student)
]
