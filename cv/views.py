from django.shortcuts import render
from .models import Education, Experience, Skills, Interests

# Create your views here.
def cv1(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skills.objects.all()
    interests = Interests.objects.all()

    return render(request, 'cv/cv1.html',{'education':education, 'experience':experience, 'skills':skills, 'interests':interests,})