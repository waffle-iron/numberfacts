from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^number/(?P<number_get>\d)$', views.view_number, name="view_number"),

]
