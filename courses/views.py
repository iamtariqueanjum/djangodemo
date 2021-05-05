from django.shortcuts import render
from django.views import View

# Create your views here.
class CourseView(View):
    template_name = 'courses/about.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    # def post(request, *args, **kwargs):
    #         return render(request, 'courses/about.html', {})

def my_fun_view(request, *args, **kwargs):
    return render(request, 'courses/about.html', {})