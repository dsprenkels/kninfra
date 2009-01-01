from django.conf.urls.defaults import *
from kn.leden.models import KnUser, KnGroup, Seat, Study
import django.views.generic.list_detail
import django.views.generic.simple
import django.views.generic.date_based

import django.views.generic as generic
from django.contrib.auth.decorators import login_required
from kn.leden import views

urlpatterns = patterns('',
	url(r'^(?:p/(?P<page>[0-9]+)/)?$',
	    login_required(generic.list_detail.object_list),
	    {'queryset':KnUser.objects.order_by('first_name').all(),
	     'paginate_by':20}, name='leden-list'),
	url(r'^gebruiker/(?P<name>[^/]+)/$',
	    views.knuser_detail, name='knuser-detail'),
	url(r'^bouwjaar/$',
	    login_required(generic.date_based.archive_index),
	    {'queryset':KnUser.objects.all(),
	     'date_field':'dateOfBirth',
	     'template_name':'leden/bouwjaar_index.html'}, 'bouwjaar-index'),
	url(r'^bouwjaar/(?P<year>[0-9]+)/$',
	    login_required(generic.date_based.archive_year),
	    {'queryset':KnUser.objects.all(),
	     'date_field':'dateOfBirth',
	     'template_name':'leden/bouwjaar.html',
	     'make_object_list':True}, name='bouwjaar'),
	url(r'^jaar/$',
	    login_required(generic.date_based.archive_index),
	    {'queryset':KnUser.objects.all(),
	     'date_field':'dateJoined',
	     'template_name':'leden/jaar_index.html'}, 'jaar-index'),
	url(r'^jaar/(?P<year>[0-9]+)/$',
	    login_required(generic.date_based.archive_year),
	    {'queryset':KnUser.objects.all(),
	     'date_field':'dateJoined',
	     'template_name':'leden/jaar.html',
	     'make_object_list':True}, name='jaar'),
	url(r'^groep/(?P<name>[^/]+)/$',
	    views.kngroup_detail, name='kngroup-detail'),
	url(r'^studie/(?P<object_id>[0-9]+)/$',
	    login_required(generic.list_detail.object_detail),
	    {'queryset':Study.objects.all()}, name='study-detail'),
	url(r'^studie/(?:page/(?P<page>[0-9]+)/)?$',
	    login_required(generic.list_detail.object_list),
	    {'queryset':Study.objects.order_by('name').all(),
	     'paginate_by':20}, name='study-list'),
	url(r'^styles/bare/$',
	    generic.simple.direct_to_template,
	    {'template':'leden/bare.css',
	     'mimetype':'text/css'}, name='style-bare'),
	url(r'^styles/common/$',
	    generic.simple.direct_to_template,
	    {'template':'leden/common.css',
	     'mimetype':'text/css'}, name='style-common'),
)
