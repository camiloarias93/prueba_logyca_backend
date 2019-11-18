from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Professor, Score, Student
from .serializers import (ProfessorSerializer, ScoreSerializer,
                          StudentSerializer)
from django.db.models import Q

class StudentAPIList(generics.ListCreateAPIView):
    lookup_field = "pk"
    serializer_class = StudentSerializer

    def get_queryset(self):
        qs = Student.objects.all()
        query = self.request.GET.get("q")
        order = self.request.GET.get("o")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query))
        if order is not None:
            qs = qs.order_by(order)
        return qs

class StudentAPI(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

class ProfessorAPIList(generics.ListCreateAPIView):
    lookup_field = "pk"
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        qs = Professor.objects.all()
        query = self.request.GET.get("q")
        order = self.request.GET.get("o")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query))
        if order is not None:
            qs = qs.order_by(order)
        return qs

class ProfessorAPI(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        return Professor.objects.all()

class ScoreAPIList(generics.ListCreateAPIView):
    lookup_field = "pk"
    serializer_class = ScoreSerializer

    def get_queryset(self):
        qs = Score.objects.all()
        query = self.request.GET.get("q")
        order = self.request.GET.get("o")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query))
        if order is not None:
            qs = qs.order_by(order)
        return qs

class ScoreAPI(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = ScoreSerializer

    def get_queryset(self):
        return Score.objects.all()