from django.shortcuts import render
from django.http import HttpResponse
from .models import Pupil


def index(request):
    return HttpResponse("Hello, world. You're at the first index..................")


def test(request, id):
    return HttpResponse("This is the test page at age of " + str(5 + id))


def get_outer_template(request):
    message = "How"
    students = Pupil.objects.filter(gender='male')


    context = {'message': message, 'students': students}
    return render(request, 'outer.html', context)


def get_inner_template(request):
    message = "This is the inner html"
    return render(request, 'pupil/inner.html', {'message': message})


# def view_pupil(request, pupil_id):
#     pupil = Pupil.objects.filter(id=pupil_id)
