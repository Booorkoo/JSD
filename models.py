import os
from django.db import models

class test(models.Model):
	el1=models.CharField(max_length=5, null=True, default=1)
	el2=models.TextField(max_length=6, null=True)
	el3=models.TextField(default=1, max_length=6)
	el4=models.TextField(max_length=6)
	el4=models.CharField(default=0)
	el5=models.CharField()

	'''
	You can chose one of these atributes to be returned instead of type object!
	def __str__(self):
		return self.el1
		return self.el2
		return self.el3
		return self.el4
		return self.el4
		return self.el5
	'''

class novi_test(models.Model):
	el11=models.TextField(max_length=5, null=True)
	el12=models.TextField(max_length=5)
	el13=models.CharField(max_length=5, null=True, default=1)
	el14=models.CharField()

	'''
	You can chose one of these atributes to be returned instead of type object!
	def __str__(self):
		return self.el11
		return self.el12
		return self.el13
		return self.el14
	'''