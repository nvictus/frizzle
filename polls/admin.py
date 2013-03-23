from django.contrib import admin
from polls.models import Instructor, Course, Session, Student, Quiz, Response

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Response)