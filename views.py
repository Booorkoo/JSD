from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import test
from .models import novi_test

class testCreateView(CreateView):
	template_name='.html'
	model=test
	fields=['el1', 'el2', 'el3', 'el4', 'el4', 'el5', ]

class novi_testCreateView(CreateView):
	template_name='.html'
	model=novi_test
	fields=['el11', 'el12', 'el13', 'el14', ]