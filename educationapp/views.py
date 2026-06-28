from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.
def get_all_student(request):
    student_list = Student.objects.all()

    return render(request, 'educationapp/student_list.html', {'students': student_list})

def get_student_by_id(request, id):
    student = get_object_or_404(Student, id = id)

    return render(request, 'educationapp/student_detail.html', {'student': student})

def filter_students(request):
    students = Student.objects.all()
    name_query = request.GET.get('name')

    if name_query:
        students = students.filter(name__icontains=name_query)
    
    age_query = request.GET.get('age')
    age_operator = request.GET.get('age_operator')

    if age_query and age_operator:
        try:
            age_value = int(age_query)
            if age_operator == 'lt':
                students = students.filter(age__lt=age_value)
            elif age_operator == 'eq':
                students = students.filter(age_value)
            elif age_operator == 'gt':
                students = students.filter(age__gt=age_value)
        except ValueError:
            pass
    
    return render(request, 'educationapp/student_list.html', {'students': students})

            



