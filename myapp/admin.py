from django.contrib import admin
from .models import Contact,FeedBack_Rating,Employee,Event,Course,Student,Student_Feedback_Rating
#admin panel customization
class Course_Admin(admin.ModelAdmin):
    list_dispaly=('course_name','course_fees','course_duration')
    list_filter=['course_fees']
    search_fields=('course_name',)

class Employee_Admin(admin.ModelAdmin):
    list_display=('emp_name','emp_email','emp_phone')
    list_filter=['emp_designation']






# Register your models here.
admin.site.register(Contact)
admin.site.register(FeedBack_Rating)
admin.site.register(Event)
admin.site.register(Employee,Employee_Admin)
admin.site.register(Course,Course_Admin)



admin.site.register(Student)
admin.site.register(Student_Feedback_Rating)





admin.site.site_header="COLLEGEADMINISTRATION"
admin.site.site_title="COLLEGEADMINDASHBOARD"
admin.site.index_title="COLLEGEADMIN"
