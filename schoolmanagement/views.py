from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from form import FormSubjects, FormStudents, FormStaff
from models import Staff, Subjects, Students


# Create your views here.


def index(request):
    return render(request, 'schoolmanagement/index.html')


def check_requester(request, requester):
    if request.method == 'GET':
        if requester == 'staff':
            form = FormStudents()
            form1 = FormSubjects()
            return render(request, 'schoolmanagement/home.html', {'form': form, 'form1': form1, 'requester': requester})
        elif requester == 'report':
            return render(request, 'schoolmanagement/report.html', {'student': Students.objects.filter(year_of_class=1),
                                                                    'classes_id': 1})
    else:
        if requester == 'staff':
            form = FormStudents(request.POST)
            form1 = FormSubjects(request.POST)
            if form.is_valid() & form1.is_valid():
                student_obj = form.save(commit=False)
                mark_obj = form1.save()
                student_obj.subjects = mark_obj
                student_obj.save()
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'schoolmanagement/index.html')


def classes(request, classes_id):
    if classes_id == '1':
        return render(request, 'schoolmanagement/report.html', {'student': Students.objects.filter(year_of_class=1),
                                                                'classes_id': 1})
    elif classes_id == '2':
        return render(request, 'schoolmanagement/report.html', {'student': Students.objects.filter(year_of_class=2),
                                                                'classes_id': 2})
    elif classes_id == '3':
        return render(request, 'schoolmanagement/report.html', {'student': Students.objects.filter(year_of_class=3),
                                                                'classes_id': 3})
    elif classes_id == '4':
        return render(request, 'schoolmanagement/report.html', {'student': Students.objects.filter(year_of_class=4),
                                                                'classes_id': 4})
    elif classes_id == '5':
        return render(request, 'schoolmanagement/report.html', {'student': Students.objects.filter(year_of_class=5),
                                                                'classes_id': 5})
    return render(request, 'schoolmanagement/index.html')


def subject_wise_mark(request, subject_name, classes_id):
    import ipdb; ipdb.set_trace()
    if classes_id == '1':
        return render(request, 'schoolmanagement/subject_wise.html', {'subject': subject_name,
                                                                      'student': Students.objects.filter(
                                                                          year_of_class=1)})
    elif classes_id == '2':
        return render(request, 'schoolmanagement/subject_wise.html', {'subject': subject_name,
                                                                      'student': Students.objects.filter(
                                                                          year_of_class=2)})
    elif classes_id == '3':
        return render(request, 'schoolmanagement/subject_wise.html', {'subject': subject_name,
                                                                      'student': Students.objects.filter(
                                                                          year_of_class=3)})
    elif classes_id == '4':
        return render(request, 'schoolmanagement/subject_wise.html', {'subject': subject_name,
                                                                      'student': Students.objects.filter(
                                                                          year_of_class=4)})
    elif classes_id == '5':
        # ls_of_studt = sort_student_with_mark(sub_name, qs = Students.objects.filter(year_of_class=5))
        return render(request, 'schoolmanagement/subject_wise.html', {'subject': subject_name,
                                                                      'student': Students.objects.filter(
                                                                          year_of_class=5).order_by(-subject_name)})
    return render(request, 'schoolmanagement/subject_wise.html')


def timetable(request, requester):
    if request.method == 'GET':
        form = FormStaff()
        form1 = FormSubjects()
        return render(request, 'schoolmanagement/home.html', {'form': form, 'form1': form1, 'requester': requester})
    else:
        form = FormStudents(request.POST)
        form1 = FormSubjects(request.POST)
        if form.is_valid() & form1.is_valid():
            pass
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'schoolmanagement/index.html')



# sort_with_mark(qs_obj)
#     sorted_qs = []
#
# print new_list
#
# def sort_student_with_mark(sub_name, qs = Students.objects.filter(year_of_class=5)):
#     if sub_name = 'TAMIL':
#         while qs_obj:
#             maxi = qs_obj[0]  # arbitrary number in list
#             for x in qs_obj:
#                 if x.tamil > maxi.tamil:
#                     maxi = x
#             sorted_qs.append(maxi)
#             data_list.remove(maxi)
#
#             return sorted_qs
