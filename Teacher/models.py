from django.db import models
from django.urls import reverse

# Create your models here.
class Teachers(models.Model):
    Level = [
        ('0', 'Grade K'),
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
    ]


    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to="gallery", blank=True)
    eduHistory = models.CharField(max_length=50)#needs 1 to many
    homeTown = models.CharField(max_length=50)
    homeState = models.CharField(max_length=2) #not required
    bio = models.TextField()
    instructionGrade = models.CharField(max_length=12, choices=Level)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teacher_detail', args=[str(self.id)])


class OfficeHours(models.Model):
    weekday=(
        ('M','Monday'),
        ('T','Tuesday'),
        ('W','Wednesday'),
        ('TH','Thursday'),
        ('F','Friday'),
    )
    #times = models.TimeField()
    days1 = models.CharField(max_length=8, choices=weekday)
    days2 = models.CharField(max_length=8, choices=weekday)
    days3 = models.CharField(max_length=8, choices=weekday)

###dont think about the physiclal callendar ui think about data
#class TutorAppointments(models.Model):
  #  hours = models.ForeinKey(OfficeHours)



#class StudentManagement(models.Model): combo of all students and teachers