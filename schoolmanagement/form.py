from models import Subjects, Staff, Students
from django.forms import ModelForm


class FormSubjects(ModelForm):

    class Meta:
        model = Subjects
        fields = ['tamil', 'telugu', 'english', 'maths', 'science', 'social']


class FormStudents(ModelForm):

    class Meta:
        model = Students
        fields = ['student_name', 'year_of_class']


class FormStaff(ModelForm):

    class Meta:
        model = Staff
        fields = ['staff_name']