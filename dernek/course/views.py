import datetime

from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import render
from django import forms

# Create your views here.
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import *


class Homepage(generic.ListView):
    model = Classroom
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)

        today = datetime.date.today()
        context['all_lectures'] = list()
        for i in range(7):
            date = today + datetime.timedelta(days=i)
            context['all_lectures'].append((date, Lecture.objects.filter(date=date)))

        context['classroom_list'] = Classroom.objects.all().order_by('name')
        context['time_of_day'] = Lecture.LECTURE_TIMES

        context['is_lecturer'] = False
        for group in self.request.user.groups.all():
            if group.name == 'Eğitmen':
                context['is_lecturer'] = True
        return context


def homepage_extension(request):
    extension_lectures = list()
    today = datetime.date.today()
    c = int(request.POST['count'])*7
    for i in range(7):
        date = today + datetime.timedelta(days=c) + datetime.timedelta(days=i)
        extension_lectures.append((date, Lecture.objects.filter(date=date)))
    classroom_list2 = Classroom.objects.all().order_by('name')
    time_of_day2 = Lecture.LECTURE_TIMES
    return render(request, 'homepage_extension.html', {'extension_lectures': extension_lectures, 'classroom_list2': classroom_list2, 'time_of_day2': time_of_day2})

 # datetime.timedelta(days=(request.POST['count']*7)) +
def hsearch_view(request):
    if request.POST['hsearch_d1'] != '' and request.POST['hsearch_d2'] != '' and len(Lecture.objects.filter(date__range=(request.POST['hsearch_d1'], request.POST['hsearch_d2']))) > 1:
        lectures = Lecture.objects.all().filter(date__range=(request.POST['hsearch_d1'], request.POST['hsearch_d2'])).order_by('date')
        classroom_list2 = Classroom.objects.all().order_by('name')
        sresults = []
        is_filtered = request.POST.get('is_filtered', False)
        if is_filtered == "on":
            is_filtered = True

        date_start = datetime.datetime.strptime(request.POST['hsearch_d1'], '%Y-%m-%d').date()
        date_end = datetime.datetime.strptime(request.POST['hsearch_d2'], '%Y-%m-%d').date()

        time_of_day2 = Lecture.LECTURE_TIMES

        if not is_filtered:
            delta = date_end - date_start
            for i in range(delta.days + 1):
                date = date_start + datetime.timedelta(days=i)
                sresults.append((date, Lecture.objects.filter(date=date)))
        else:
            for a in lectures:
                date = a.date
                sresults.append((date, Lecture.objects.filter(date=date)))

        is_lecturer = False
        for group in request.user.groups.all():
            if group.name == 'Eğitmen':
                is_lecturer = True
        return render(request, 'hsearch.html', {'is_filtered': is_filtered, 'is_lecturer': is_lecturer, 'slectures': lectures, 'sresults': sresults, 'classroom_list2': classroom_list2, 'time_of_day2': time_of_day2})
    else:
        return JsonResponse(data='Geçersiz Arama Kriterleri! (İkiden az ders girdisi ya da geçersiz tarih formatı)', safe=False)


def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if user:
        login(request, user)
        return JsonResponse(data='Giriş yapıldı.', safe=False)
    else:
        return JsonResponse(data='Hatalı kullanıcı adı ya da şifre.', safe=False)


@csrf_exempt
def logout_view(request):
    logout(request)

    return JsonResponse(data='Çıkış yapıldı.', safe=False)


def add_lecture_view(request):
    if request.POST['lecture_name'] != '':
        Lecture.objects.create(
            name=request.POST['lecture_name'],
            classroom=Classroom.objects.filter(name=request.POST['classroom']).first(),
            lecture_time=request.POST['time'],
            date=request.POST['date'],
            lecturer=request.user,
            students=request.POST['students'],
        )
        return JsonResponse(data='Ders kaydedildi.', safe=False)
    else:
        return JsonResponse(data='Ders adı kısmı boş bırakılamaz.', safe=False)


def delete_lecture_view(request):
    try:
        Lecture.objects.get(
            name=request.POST['lecture_name'],
            classroom=Classroom.objects.filter(name=request.POST['classroom']).first(),
            lecture_time=request.POST['time'],
            date=request.POST['date'],
            lecturer=request.user,
        ).delete()
    except Lecture.DoesNotExist:
        return JsonResponse(data='Bir hata oluştu.', safe=False)

    return JsonResponse(data='Ders başarılı bir şekilde silindi', safe=False)


def register_view(request):
    if User.objects.filter(username=request.POST['username']):
        return JsonResponse(data='Girilen kullanıcı adı zaten mevcut. Farklı bir kullanıcı adı seçerek tekrar deneyin.', safe=False)
    elif request.POST['first_name'] == '' or request.POST['last_name'] == '':
        return JsonResponse(data='Ad, Soyad alanlarının doldurulması zorunludur.', safe=False)
    elif len(request.POST['username']) < 3:
        return JsonResponse(data='Kullanıcı adı 3 karakterden daha az olamaz.', safe=False)
    elif request.POST['pass_first'] != request.POST['pass_second']:
        return JsonResponse(data='Girilen şifreler aynı değil.', safe=False)
    elif len(request.POST['pass_first']) < 6:
        return JsonResponse(data='Şifre 6 karakterden daha az olamaz', safe=False)
    else:
        User.objects.create_user(username=request.POST['username'],
                                 first_name=request.POST['first_name'],
                                 last_name=request.POST['last_name'],
                                 email=request.POST['email'],
                                 password=request.POST['pass_first'])

        return JsonResponse(data='Başarılı bir şekilde kayıt oldunuz.', safe=False)
