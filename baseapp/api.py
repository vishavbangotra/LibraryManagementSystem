from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Book, Student, Author
from .serializer import BookSerializer, StudentSerializer

# .queries module contain all the sql queries
from .queries import Query

# Get all books
@api_view(["GET", "POST"])
@permission_classes((permissions.AllowAny,))
def get_all_books(request):
    if request.method == "GET":
        books = Book.objects.raw(Query.getBookAll)
        serilizer_class = BookSerializer(books, many=True)
        return Response(serilizer_class.data)

    elif request.method == "POST":
        serilizer_class = BookSerializer(request.data, many=True)
        if serilizer_class.is_valid():
            serilizer_class.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
        



# Get book by id
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_book_by_id(request, pk):
    book = Book.objects.raw(Query.getBookById, [pk])
    serilizer_class = BookSerializer(book, many=True)
    return Response(serilizer_class.data)

# Get Student by id
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_student_detail(request, pk):
    student = Student.objects.raw(Query.getStudentById, [pk])
    serializer_class = StudentSerializer(student, many=True)
    return Response(serializer_class.data)



