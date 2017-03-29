from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import test
from .models import novi_test

#Create view for test model.
class testCreateView(CreateView):
	template_name='.html'
	model=test
	fields=['el1', 'el2', 'el3', 'el4', 'el4', 'el5']
	success_url=reverse_lazy('')

#Update view for test model.
class testUpdateView(UpdateView):
	template_name='.html'
	model=test
	fields=['el1', 'el2', 'el3', 'el4', 'el4', 'el5']

#Delete view for test model.
class testDeleteView(DeleteView):
	template_name='.html'
	model=test
	success_url=reverse_lazy('')

#Create view for novi_test model.
class novi_testCreateView(CreateView):
	template_name='.html'
	model=novi_test
	fields=['el11', 'el12', 'el13', 'el14']
	success_url=reverse_lazy('')

#Update view for novi_test model.
class novi_testUpdateView(UpdateView):
	template_name='.html'
	model=novi_test
	fields=['el11', 'el12', 'el13', 'el14']

#Delete view for novi_test model.
class novi_testDeleteView(DeleteView):
	template_name='.html'
	model=novi_test
	success_url=reverse_lazy('')