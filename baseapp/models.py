from ast import For
from contextlib import nullcontext
from enum import unique
from typing import List
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import (Model, DateTimeField, CASCADE, OneToOneField,
                              BooleanField, ForeignKey, DateField,
                              CharField, IntegerField, BigIntegerField)


class Student(Model):
    reg_num = BigIntegerField(primary_key=True)
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    fine = IntegerField(blank=True, null=True)
    dob = DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name


class Author(Model):
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)

    def __str__(self):
        return self.first_name + self.last_name


class Issue(Model):
    issued_to = ForeignKey(Student, on_delete=CASCADE)
    issue_date = DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Issued to " + self.issued_to + " on " + self.issue_date


class Book(Model):
    name = CharField(max_length=256, default="name")
    author = ForeignKey(Author, on_delete=CASCADE)
    issue = OneToOneField(Issue, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
