from django.shortcuts import render
from .models import Classroom
from .models import Office
from .models import Miscellaneous
from .models import FacultyRoom
from django.http import HttpResponse
# Create your views here.

def page(request):
    position = request.GET['FinalPosition']

    dict={'room_no' : '000'}

    classrooms = Classroom.objects
    list1 = list(classrooms.values())

    for i in range(len(list1)):
        if list1[i]['room_no']==position :
            dict=list1[i]
            break

    facultyrooms = FacultyRoom.objects
    list2 = list(facultyrooms.values())

    for i in range(len(list2)) :
        if list2[i]['Name']==position :
            dict=list2[i]
            break

    floor = dict['room_no'][0]

    if floor == '1':
        return render(request, 'acad_first_floor.html', {'room_no':dict['room_no'], 'image':dict['images']})
    elif floor == '2':
        return render(request, 'acad_second_floor.html', {'room_no':dict['room_no'], 'image':dict['images']})
    elif floor == '3':
        return render(request, 'acad_third_floor.html', {'room_no':dict['room_no'], 'image':dict['images']})
    else :
        return render(request, 'search_error.html')


def search(request):
    return render(request, 'search.html')
