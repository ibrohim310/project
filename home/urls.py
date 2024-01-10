from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('about.html',about),
    path('courses.html',courses),
    path('course_details.html',course_d),
    path('elements.html',elements),
    path('blog.html',blogs),
    path('single-blog.html',single_b),
    path('contact.html',contact),
    path('index.html',index)

]