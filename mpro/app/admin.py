from django.contrib import admin
from .models import AdminProfile, Dep, TeacherProfile,Sec,StudentProfile, TecherMainProfile,StudentsMainProfile, Attendencemodel,StudentEvulate,TeacherEvulate


admin.site.register(AdminProfile),
admin.site.register(Dep),
admin.site.register(Attendencemodel),
admin.site.register(StudentsMainProfile)
admin.site.register(TeacherEvulate)
admin.site.register(StudentEvulate)
admin.site.register(TeacherProfile),
admin.site.register(TecherMainProfile),
admin.site.register(Sec),
admin.site.register(StudentProfile)



