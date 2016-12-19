from django.conf.urls import url

from . import views

app_name = 'login_reg'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register$', views.register, name='register'),
	url(r'^success$', views.success, name='success'),
	url(r'^login$', views.login, name='login'),

]
