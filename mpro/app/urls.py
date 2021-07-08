from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
     path("profile/",views.ProfileView.as_view(),name="profile"),
     path('teacher/',views.TeacherAccountView.as_view()),
     path('teacher/<int:pk>', views.TeacherAccountView_detail.as_view(), name=''),
     path('dep/',views.DepView.as_view(), name='' ),
     path('dep/<int:pk>', views.DepView_detail.as_view(), name=''),
     path('teacherspro', views.TecherPofileView.as_view(), name='teacherspro'),
     path('teacherspro/<int:pk>', views.TecherPofileView_detail.as_view()),
     path('students/', views.StudentView.as_view()),
     path('students/<int:pk>', views.StudentView_detail.as_view()),
     path('attendence/', views.AttView.as_view()),
     path('attendence/<int:pk>', views.Att_detail.as_view()),
     path('students_evolution/', views.StudentEvulateView.as_view()),
     path('teacher_evolution/', views.teacherEvulateView.as_view()),
     path('student_profile',views.StudentProfileview.as_view()),
     path('student_profile/<int:pk>', views.StudentProfileview_Details.as_view())




]
urlpatterns = format_suffix_patterns(urlpatterns)