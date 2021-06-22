from django.contrib import admin
from .models import AdminProfile, Dep, TeacherProfile,Sec,StudentProfile


admin.site.register(AdminProfile),
admin.site.register(Dep),

admin.site.register(TeacherProfile),
admin.site.register(Sec),
admin.site.register(StudentProfile)

