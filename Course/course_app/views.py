from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

# Barcha kurslarni ko'rsatish
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# Kursga tegishli darslarni ko'rsatish
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})

# Darsning batafsil ma'lumotini ko'rsatish
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
