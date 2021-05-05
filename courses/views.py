from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Course

# Create your views here.
class CourseView(View):
    template_name = 'courses/about.html'
    def get(self, request, *args, **kwargs):
        obj =  Course.objects.all()
        context = {
            "object":obj
        }
        return render(request, self.template_name, context)
    # def post(request, *args, **kwargs):
    #         return render(request, 'courses/about.html', {})

class CourseDetailView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, id=None, *args, **kwargs):
        context = {"object_list":self.get_queryset()}
        return render(request, self.template_name, context)

# class MyCourseListView(CourseListView):
#     queryset = Course.objects.filter(id=1)

def my_fun_view(request, *args, **kwargs):
    return render(request, 'courses/about.html', {})