from django.urls import path
from .views import my_fun_view,CourseView,CourseDetailView

app_name = 'courses'

urlpatterns = [
    #path('', my_fun_view, name='courses-list'),
    # path('',CourseView.as_view(template_name='contact.html'), name='course-list'),
    path('',CourseView.as_view(), name='course-list'),
    path('<int:id>',CourseDetailView.as_view(), name='course-detail'),
]