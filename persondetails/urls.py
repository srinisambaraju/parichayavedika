from django.conf.urls import url

from .import views
# comment
# adding new comments
urlpatterns = [

    url(r'^$', views.person_list)
]