"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .api import StudentAPI, StudentAPIList, ProfessorAPI, ProfessorAPIList, ScoreAPI, ScoreAPIList

urlpatterns = [
    path('students', StudentAPIList.as_view(), name="api_list_create_student"),
    path('students/<int:pk>', StudentAPI.as_view(), name="api_modify_delete_student"),
    path('professors', ProfessorAPIList.as_view(), name="api_create_professor"),
    path('professors/<int:pk>', ProfessorAPI.as_view(), name="api_modify_delete_professor"),
    path('scores', ScoreAPIList.as_view(), name="api_create_score"),
    path('scores/<int:pk>', ScoreAPI.as_view(), name="api_modify_delete_score"),
]
