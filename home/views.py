from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Speciality,Courses

def main(request):
    blogs = Blog.objects.all()
    courses = Courses.objects.all()
    specialitys = Speciality.objects.all()

    context = {
        'blogs':blogs,
        'courses':courses,
        'specialitys':specialitys,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def course_d(request):
    return render(request, 'course_details.html')

def elements(request):
    return render(request, 'elements.html')

def blogs(request):
    return render(request, 'blog.html')

def single_b(request):
    return render(request, 'single-blog.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')




