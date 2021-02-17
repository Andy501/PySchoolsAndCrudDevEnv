from django.db import models
from Teacher.models import Teachers
from django.urls import reverse

#
class MemberStudent(models.Model):
     instructor = models.ForeignKey(Teachers, on_delete=models.CASCADE)
     name = models.CharField(max_length=50, default="Doe")
     age = models.IntegerField(default=99)


     def __str__(self):
          return self.name

     def get_absolute_url(self):
          return reverse('student_detail', args=[str(self.id)])

class BehaviorGrade(models.Model):
    SEVERITY = [
        ('Bad','Bad Behavior'),
        ('Good','Good Behavior'),
        ('Danger','Dangerous'),
    ]

    LETTER_GRADE = [
        ('A','A'),
        ('B','B'),
        ('F','F'),
    ]

    studentName = models.ForeignKey(MemberStudent, on_delete=models.CASCADE, null=True) #need a link to student name
    eventGrade = models.CharField(max_length=1, choices=LETTER_GRADE)
    eventSeverity = models.CharField(max_length=15, choices=SEVERITY)
    eventTitle = models.CharField(max_length=15)
    eventDescription = models.TextField()

    def __str__(self):
        return self.eventTitle