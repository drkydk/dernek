from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view()),
    url(r'^login$', views.login_view),
    url(r'^logout$', views.logout_view),
    url(r'^add-lecture$', views.add_lecture_view),
    url(r'^register$', views.register_view),
    url(r'^delete-lecture$', views.delete_lecture_view),
    url(r'^hsearch', views.hsearch_view, name='hsearch'),
    url(r'^homepage_extension', views.homepage_extension)
]
