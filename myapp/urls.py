from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('mark-attendence/', views.mark_attendence, name='mark_attendence'),
    path('faculty-dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('faculty-mark',views.faculty_mark,name='faculty_mark'),
    path('stviewreport/', views.stviewreport, name='stviewreport'),
    path('logout/', views.logout_view, name='logout'),
]
