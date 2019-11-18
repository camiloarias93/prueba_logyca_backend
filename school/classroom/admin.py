from django.contrib import admin
from .models import Student, Professor, Score

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Score)