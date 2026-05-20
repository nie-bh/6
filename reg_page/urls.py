from django.urls import path 
from reg_page.views import * 
from .views import StudentListView, StudentDetailView, StudentDeleteView
urlpatterns = [ 
    path('mainpage/', home1, name='home1'), 
    path('studentlist/', studentlist, name='studentlist'), 
    path('courselist/', courselist, name='courselist'), 
    path('register/', register, name='register'), 
    path('enrolledlist/', enrolledStudents, name='enrolledStudents'), 
    path('unenroll/<int:student_id>/<int:course_id>/', unenroll, name='unenroll'),
    path('students/', StudentListView.as_view(), name='student-list'), 
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'), 
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
] 
