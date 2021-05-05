from django.urls import path
from .views import (
    my_fun_view,
    CourseView,
    CourseDetailView,
    CourseListView,
    # MyCourseListView
    CourseCreateView
)

app_name = 'courses'

urlpatterns = [
    #path('', my_fun_view, name='courses-list'),
    # path('',CourseView.as_view(template_name='contact.html'), name='course-list'),
    path('', CourseListView.as_view(), name='course-list'),
    # path('first',MyCourseListView.as_view(), name='course-list-first'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/', CourseDetailView.as_view(), name='course-detail'),
]