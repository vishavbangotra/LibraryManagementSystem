from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from .models import Book, Student, Author
from .serializers import BookSerializer, StudentSerializer, IssueSerializer
# .queries module contain all the sql queries
from .queries import Query
# Get all books


@api_view(["GET", "POST"])
@csrf_exempt
@permission_classes((permissions.AllowAny,))
def get_all_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer_class = BookSerializer(books, many=True)
        return Response(serializer_class.data)

    elif request.method == "POST":
        serializer_class = BookSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Search Book by name
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def search_book_by_name(request, param_name):
    param_name = "%" + param_name + "%"
    books = Book.objects.raw(Query.selectBooksByName, [param_name])
    serializer_class = BookSerializer(books, many=True)
    return Response(serializer_class.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def issue_book_by_student(request):
    serializer_class = IssueSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Get book by id


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_book_by_id(request, pk):
    book = Book.objects.raw(Query.getBookById, [pk])
    serilizer_class = BookSerializer(book, many=True)
    return Response(serilizer_class.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_books_by_category(request, param_name):
    books = Book.objects.filter(category=param_name)
    serializer_class = BookSerializer(books, many=True)
    return Response(serializer_class.data)


# Get All students list
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_all_students(request):
    students = Student.objects.raw(Query.getAllStudents)
    serializer_class = StudentSerializer(students, many=True)
    return Response(serializer_class.data)


# Get Student by id
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_student_detail(request, pk):
    student = Student.objects.raw(Query.getStudentById, [pk])
    serializer_class = StudentSerializer(student, many=True)
    return Response(serializer_class.data)
