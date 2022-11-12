from django.db import models
from django.db.models import (Model, DateTimeField, CASCADE, OneToOneField,
                              BooleanField, ForeignKey, DateField,
                              CharField, IntegerField, BigIntegerField)

import datetime


class Student(Model):
    name = CharField(max_length=128)
    fine = IntegerField(default=0)
    dob = DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(Model):
    name = CharField(max_length=127)

    def __str__(self):
        return self.name


categories = [('any', 'Any'), ('Fiction', 'Fiction'), ('Non-fiction', 'Non-fiction'), ('Horror',
                                                                                       'Horror'), ('Drama', 'Drama'), ('Engineering', 'Engineering'), ('Competitive', "Competitive")]


class Book(Model):
    name = CharField(max_length=256)
    category = CharField(max_length=255, choices=categories)
    author = ForeignKey(Author, on_delete=CASCADE)
    copies_left = IntegerField()

    def __str__(self):
        return self.name


class Issue(Model):
    book_id = ForeignKey(Book, on_delete=CASCADE)
    issued_to = ForeignKey(Student, on_delete=CASCADE)
    issue_date = DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return "Issued to " + str(self.issued_to.name) + " on " + str(self.issue_date)
