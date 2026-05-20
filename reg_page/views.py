from django.shortcuts import render, redirect 
from reg_page.models import student, course 
from django.views import generic 
from django.urls import reverse_lazy
 
def home1(request): 
    return render(request, 'homepage.html') 
 
def studentlist(request): 
    students = student.objects.all() 
    return render(request, 'studentlist.html', {'student_list': students}) 
 
def courselist(request): 
    courses = course.objects.all() 
    return render(request, 'courselist.html', {'course_list': courses}) 
 
def register(request): 
    if request.method == "POST": 
        student_id = request.POST.get('student') 
        course_id = request.POST.get('course') 
        selected_student = student.objects.get(id=student_id) 
        selected_course = course.objects.get(id=course_id) 
        selected_student.enrollment.add(selected_course) 
        return redirect('/enrolledlist/') 
    students = student.objects.all() 
    courses = course.objects.all() 
    return render(request, 'register.html', {'student_list': students, 'course_list': courses}) 
 
def enrolledStudents(request): 
    course_list = course.objects.all() 
    student_list = None 
    selected_course = None 
    if request.method == "POST": 
        course_id = request.POST.get('course') 
        selected_course = course.objects.get(id=course_id) 
        student_list = selected_course.students.all() 
    return render(request, 'enrolledlist.html', { 
        'Course_List': course_list, 
        'student_list': student_list, 
        'course': selected_course 
    }) 
 
class StudentListView(generic.ListView):  
    model = student  
    template_name = "GenericListViewStudent.html"  
 
class StudentDetailView(generic.DetailView):  
    model = student  
    template_name = "GenericDetailedViewStudent.html" 

class StudentDeleteView(generic.DeleteView):
    model = student
    template_name = "GenericDeleteViewStudent.html"
    success_url = reverse_lazy('student-list')

def unenroll(request, student_id, course_id):
    s = student.objects.get(id=student_id)
    c = course.objects.get(id=course_id)
    s.enrollment.remove(c)
    
    # Re-render the enrolledlist page with the updated student list for the same course
    course_list = course.objects.all()
    student_list = c.students.all()
    return render(request, 'enrolledlist.html', {
        'Course_List': course_list,
        'student_list': student_list,
        'course': c
    })
