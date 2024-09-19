from django.urls import path,include
from .import views,student_views
urlpatterns=[
    path("",views.home,name="home"),
    path("about/",views.about_us,name="about"),
    path("feedback/",views.feedback,name="feedback"),
    path("contact/",views.contact,name="contact"),
    path("cources/",views.cources,name="cources"),
    # path("login/",student_views.login,name="login"),
    path("login/",student_views.Login.as_view(),name="login"),

    path("employee/",views.employee_details,name="employee"),
    path("student_home/",student_views.show_home,name="student_home"),
    path("logout/",student_views.logout,name="logout"),
    path("student_edit_profile/",student_views.student_edit_profile,name="student_edit_profile"),
    path("student_feedback_rating/",student_views.student_feedback_rating,name="student_feedback_rating"),
]