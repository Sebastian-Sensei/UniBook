# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import View
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from app1.models import App1

class ListadoView(View):
	"""docstring for TodoListView"""
	def get(self, request, *args, **kwargs):
		context = {
			'listado': App1.objects.all()
		}
		return TemplateResponse(request, 'listado.html', context)
		

class ListadoAddView(View):
	def get(self, request, *args, **kwargs):
		return TemplateResponse(request, 'listado_add.html', {})

	def post(self, request, *args, **kwargs):
		description = request.POST['description']
		App1.objects.create(description=description)
		return HttpResponseRedirect('/')

class ListadoDoneView(View):
	def get(self, request, *args, **kwargs):
		listado = App1.objects.get(id=kwargs['listado_id'])
		listado.is_done = True
		listado.save()
		return HttpResponseRedirect('/')
		

# Create your views here.
