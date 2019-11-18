from rest_framework import serializers
from .models import Student, Professor, Score

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "pk",
            "name"
        ]


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professor
        fields = [
            "pk",
            "name"
        ]

class ScoreSerializer(serializers.ModelSerializer):

    professor = serializers.PrimaryKeyRelatedField(many=False, queryset=Professor.objects.all())
    student = serializers.PrimaryKeyRelatedField(many=False, queryset=Student.objects.all())
    class Meta:
        model = Score
        fields = [
            "pk",
            "name",
            "value",
            "professor",
            "student"
        ]
        depth = 3
