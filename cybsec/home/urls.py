from django.conf.urls import url
from . import views 

urlpatterns = [

	url(r'^$', views.index),
	url(r'^Projects$',views.projects),
	url(r'^team$',views.team),
	url(r'^home$',views.index)
	]
