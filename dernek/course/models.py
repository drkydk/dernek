from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=250, verbose_name='derslik adı')
    quota = models.IntegerField(verbose_name='kontenjan')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'derslik'
        verbose_name_plural = 'derslikler'


class Lecture(models.Model):
    LECTURE_TIMES = (
        (9, '09:00 - 09:45'),
        (10, '10:00 - 10:45'),
        (11, '11:00 - 11:45'),
        (12, '12:00 - 12:45'),
        (13, '13:00 - 13:45'),
        (14, '14:00 - 14:45'),
        (15, '15:00 - 15:45'),
        (16, '16:00 - 16:45'),
        (17, '17:00 - 17:45'),
        (18, '18:00 - 18:45'),
        (19, '19:00 - 19:45'),
        (20, '20:00 - 20:45'),
    )

    name = models.CharField(max_length=250, verbose_name='ders adı')
    date = models.DateField(verbose_name='tarih')
    lecture_time = models.SmallIntegerField(choices=LECTURE_TIMES, verbose_name='ders saati')
    lecturer = models.ForeignKey(User, verbose_name='eğitmen')
    classroom = models.ForeignKey(Classroom, verbose_name='derslik')
    students = models.TextField(verbose_name='öğrenciler')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ders'
        verbose_name_plural = 'Dersler'
