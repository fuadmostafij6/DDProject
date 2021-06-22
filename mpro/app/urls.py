from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
     path("profile/",views.ProfileView.as_view(),name="profile"),
     path('teacher/',views.TeacherAccountView.as_view()),
     path('teacher/<int:pk>', views.TeacherAccountView_detail.as_view(), name=''),
     path('dep/',views.DepView.as_view(), name='' ),
     path('dep/<int:pk>', views.DepView_detail.as_view(), name='')



]
urlpatterns = format_suffix_patterns(urlpatterns)