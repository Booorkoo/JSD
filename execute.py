'''
Created on 06.12.2015.

@author: xx
'''

from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot, os


class Proba(object):
    def __init__(self):
        self.query_set = []

    def interpreter(self, model):

        return self.query_set


def execute(path, grammar_file_name, example_file_name, export_dot, export_png):
    '''U svrhe brzeg testiranja, metoda koja prima putanju do foldera, naziv fajla gde je gramatika i naziv fajla gde je
        primer programa u nasem jeziku i indikator da li da se eksportuju .dot i .png fajlovi'''

    meta_path = os.path.join(path, grammar_file_name)
    meta_name = os.path.splitext(meta_path)[0]
    metamodel = metamodel_from_file(meta_path)

    if export_dot:
        metamodel_export(metamodel, meta_name + '.dot')
        if export_png:
            graph = pydot.graph_from_dot_file(meta_name + '.dot')
            #graph[0].write_png(meta_name + '.png')

    model_path = os.path.join(path, example_file_name)
    model_name = os.path.splitext(model_path)[0]

    model = metamodel.model_from_file(model_path)

    if export_dot:
        model_export(model, model_name + '.dot')
    if export_png:
        graph = pydot.graph_from_dot_file(model_name + '.dot')
        #graph[0].write_png(model_name + '.png')

    #print(model.models[0].elements[0].datatype.charfield.parameters[0].max_length.number)
    '''proba = Proba()
    query_set = []
    query_set = proba.interpreter(model)'''

    models = model.models
    models1 = []
    for model in models:
        elements = model.elements
        dict = {}
        #elements1 = []
        dict['model'] = model.name
        dict['elements'] = elements
        '''for element in elements:
            dict['name'] = element.name
            if element.datatype.charfield is not None:
                dict['DataType'] = 'CharField'
                dict['maxLength'] = element.datatype.charfield.parameters[0].max_length.number
                dict['null'] = element.datatype.charfield.parameters[1].null.value
            else:
                dict['DataType'] = 'TextField'
                dict['maxLength'] = element.datatype.textfield.parameters[0].max_length.number
                dict['null'] = element.datatype.textfield.parameters[1].null.value'''
        print(dict)
        models1.append(dict)

    print('bla bla')
    print(models1)

    def test(models):
        string = 'from __future__ import unicode_literals\n\nfrom django.db import migrations, models\nimport django.db.models.deletion\nimport django.utils.timezone\n\n\nclass Migration(migrations.Migration):\n\n\tinitial = True\n\n\tdependencies = [\n\t]\n\n\toperations = ['
        for model in models:
            string += '\n\t\t'
            string += 'migrations.CreateModel('
            string += '\n\t\t\tname=' + "'" + str(model['model']) + "',"
            string += '\n\t\t\tfields=['
            string += '\n\t\t\t\t(' + "'id'" + ",models.AutoField" + "(auto_created=True, primary_key=True, serialize=False, verbose_name=" + "'ID')),"
            for element in model['elements']:
                string += '\n\t\t\t\t(' + "'"
                string += element.name + "'," + "models."
                if element.datatype.charfield is not None:
                    string += 'CharField' + "("

                    if len(element.datatype.charfield.parameters) == 0:
                        string += ")),"

                    elif len(element.datatype.charfield.parameters) == 1:
                        if element.datatype.charfield.parameters[0].max_length is not None:
                            string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ")),"
                        if element.datatype.charfield.parameters[0].null is not None:
                            string += 'null=' + element.datatype.charfield.parameters[0].null.value + ")),"
                        if element.datatype.charfield.parameters[0].default is not None:
                            string += 'default=' + element.datatype.charfield.parameters[0].default.number + ")),"

                    elif len(element.datatype.charfield.parameters) == 3:
                        string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.charfield.parameters[1].null.value + ", "
                        string += 'default=' + element.datatype.charfield.parameters[2].default.number + ")),"

                    elif element.datatype.charfield.parameters[0].max_length and element.datatype.charfield.parameters[1].null is not None:
                        string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.charfield.parameters[1].null.value + ")),"

                    elif element.datatype.charfield.parameters[0].null and element.datatype.charfield.parameters[1].max_length is not None:
                        string += 'null=' + element.datatype.charfield.parameters[0].null.value + ", "
                        string += 'max_length=' + element.datatype.charfield.parameters[1].max_length.number + ")),"

                    elif element.datatype.charfield.parameters[0].max_length and element.datatype.charfield.parameters[1].default is not None:
                        string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ", "
                        string += 'default=' + element.datatype.charfield.parameters[1].default.number + ")),"

                    elif element.datatype.charfield.parameters[0].default and element.datatype.charfield.parameters[1].max_length is not None:
                        string += 'default=' + element.datatype.charfield.parameters[0].default.number + ", "
                        string += 'max_length=' + element.datatype.charfield.parameters[1].max_length.number + ")),"

                    elif element.datatype.charfield.parameters[0].null and element.datatype.charfield.parameters[1].default is not None:
                        string += 'null=' + element.datatype.charfield.parameters[0].null.value + ","
                        string += 'default=' + element.datatype.charfield.parameters[1].default.number + ")),"

                    elif element.datatype.charfield.parameters[0].default and element.datatype.charfield.parameters[1].null is not None:
                        string += 'default=' + element.datatype.charfield.parameters[0].default.number + ", "
                        string += 'null=' + element.datatype.charfield.parameters[1].null.value + ")),"

                else:
                    string += 'TextField' + "("

                    if len(element.datatype.textfield.parameters) == 0:
                        string += ")),"

                    if len(element.datatype.textfield.parameters) == 1:
                        if element.datatype.textfield.parameters[0].max_length is not None:
                            string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ")),"
                        if element.datatype.textfield.parameters[0].null is not None:
                            string += 'null=' + element.datatype.textfield.parameters[0].null.value + ")),"
                        if element.datatype.textfield.parameters[0].default is not None:
                            string += 'default=' + element.datatype.textfield.parameters[0].default.number + ")),"

                    elif len(element.datatype.textfield.parameters) == 3:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ", "
                        string += 'default=' + element.datatype.textfield.parameters[2].default.number + ")),"

                    elif element.datatype.textfield.parameters[0].max_length and element.datatype.textfield.parameters[1].null is not None:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ")),"

                    elif element.datatype.textfield.parameters[0].null and element.datatype.textfield.parameters[1].max_length is not None:
                        string += 'null=' + element.datatype.textfield.parameters[0].null.value + ","
                        string += 'max_length=' + element.datatype.textfield.parameters[1].max_length.number + ")),"

                    elif element.datatype.textfield.parameters[0].max_length and element.datatype.textfield.parameters[1].default is not None:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'default=' + element.datatype.textfield.parameters[1].default.number + ")),"

                    elif element.datatype.textfield.parameters[0].default and element.datatype.textfield.parameters[1].max_length is not None:
                        string += 'default=' + element.datatype.textfield.parameters[0].default.number + ", "
                        string += 'max_length=' + element.datatype.textfield.parameters[1].max_length.number + ")),"

                    elif element.datatype.textfield.parameters[0].null and element.datatype.textfield.parameters[1].default is not None:
                        string += 'null=' + element.datatype.textfield.parameters[0].null.value + ","
                        string += 'default=' + element.datatype.textfield.parameters[1].default.number + ")),"

                    elif element.datatype.textfield.parameters[0].default and element.datatype.textfield.parameters[1].null is not None:
                        string += 'default=' + element.datatype.textfield.parameters[0].default.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ")),"

            string += '\n\t\t\t],'
            string += '\n\t\t),'
        string += '\n\t]'
        return string


    with open('C:/Users/Johny/Desktop/mrk/mysite/myapp/migrations/0001_initial.py', 'w') as f:
        a = test(models1)
        f.write(a)


    def test1(models):
        string = 'import os\nfrom django.db import models'
        for model in models:
            string += '\n\nclass '
            string += str(model['model']) + "(" + 'models.Model' + "):"
            for element in model['elements']:
                string += '\n\t'
                string += element.name + "=" + "models."
                if element.datatype.charfield is not None:
                    string += 'CharField' + "("

                    if len(element.datatype.charfield.parameters) == 0:
                        string += ")"

                    elif len(element.datatype.charfield.parameters) == 1:
                        if element.datatype.charfield.parameters[0].max_length is not None:
                            string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ")"
                        if element.datatype.charfield.parameters[0].null is not None:
                            string += 'null=' + element.datatype.charfield.parameters[0].null.value + ")"
                        if element.datatype.charfield.parameters[0].default is not None:
                            string += 'default=' + element.datatype.charfield.parameters[0].default.number + ")"

                    elif len(element.datatype.charfield.parameters) == 3:
                        string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.charfield.parameters[1].null.value + ", "
                        string += 'default=' + element.datatype.charfield.parameters[2].default.number + ")"

                    elif element.datatype.charfield.parameters[0].max_length and element.datatype.charfield.parameters[1].null is not None:
                        string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.charfield.parameters[1].null.value + ")"

                    elif element.datatype.charfield.parameters[0].null and element.datatype.charfield.parameters[1].max_length is not None:
                        string += 'null=' + element.datatype.charfield.parameters[0].null.value + ", "
                        string += 'max_length=' + element.datatype.charfield.parameters[1].max_length.number + ")"

                    elif element.datatype.charfield.parameters[0].max_length and element.datatype.charfield.parameters[1].default is not None:
                        string += 'max_length=' + element.datatype.charfield.parameters[0].max_length.number + ", "
                        string += 'default=' + element.datatype.charfield.parameters[1].default.number + ")"

                    elif element.datatype.charfield.parameters[0].default and element.datatype.charfield.parameters[1].max_length is not None:
                        string += 'default=' + element.datatype.charfield.parameters[0].default.number + ", "
                        string += 'max_length=' + element.datatype.charfield.parameters[1].max_length.number + ")"

                    elif element.datatype.charfield.parameters[0].null and element.datatype.charfield.parameters[1].default is not None:
                        string += 'null=' + element.datatype.charfield.parameters[0].null.value + ","
                        string += 'default=' + element.datatype.charfield.parameters[1].default.number + ")"

                    elif element.datatype.charfield.parameters[0].default and element.datatype.charfield.parameters[1].null is not None:
                        string += 'default=' + element.datatype.charfield.parameters[0].default.number + ", "
                        string += 'null=' + element.datatype.charfield.parameters[1].null.value + ")"

                else:
                    string += 'TextField' + "("

                    if len(element.datatype.textfield.parameters) == 0:
                        string += ")"

                    if len(element.datatype.textfield.parameters) == 1:
                        if element.datatype.textfield.parameters[0].max_length is not None:
                            string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ")"
                        if element.datatype.textfield.parameters[0].null is not None:
                            string += 'null=' + element.datatype.textfield.parameters[0].null.value + ")"
                        if element.datatype.textfield.parameters[0].default is not None:
                            string += 'default=' + element.datatype.textfield.parameters[0].default.number + ")"

                    elif len(element.datatype.textfield.parameters) == 3:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ", "
                        string += 'default=' + element.datatype.textfield.parameters[2].default.number + ")"

                    elif element.datatype.textfield.parameters[0].max_length and element.datatype.textfield.parameters[1].null is not None:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ")"

                    elif element.datatype.textfield.parameters[0].null and element.datatype.textfield.parameters[1].max_length is not None:
                        string += 'null=' + element.datatype.textfield.parameters[0].null.value + ","
                        string += 'max_length=' + element.datatype.textfield.parameters[1].max_length.number + ")"

                    elif element.datatype.textfield.parameters[0].max_length and element.datatype.textfield.parameters[1].default is not None:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'default=' + element.datatype.textfield.parameters[1].default.number + ")"

                    elif element.datatype.textfield.parameters[0].default and element.datatype.textfield.parameters[1].max_length is not None:
                        string += 'default=' + element.datatype.textfield.parameters[0].default.number + ", "
                        string += 'max_length=' + element.datatype.textfield.parameters[1].max_length.number + ")"

                    elif element.datatype.textfield.parameters[0].null and element.datatype.textfield.parameters[1].default is not None:
                        string += 'null=' + element.datatype.textfield.parameters[0].null.value + ","
                        string += 'default=' + element.datatype.textfield.parameters[1].default.number + ")"

                    elif element.datatype.textfield.parameters[0].default and element.datatype.textfield.parameters[1].null is not None:
                        string += 'default=' + element.datatype.textfield.parameters[0].default.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ")"

            string += '\n\n\t'
            string += "'''"
            string += '\n\tYou can chose one of these atributes to be returned instead of type object!'
            string += '\n\tdef __str__(self):'
            for element in model['elements']:
                string += '\n\t\treturn self.' + element.name
            string += '\n\t' + "'''"
        return string

    with open('C:/Users/Johny/Desktop/mrk/mysite/myapp/models.py', 'w') as f:
        a = test1(models1)
        f.write(a)

    def test2(models):
        string = 'from django.views import generic\nfrom django.views.generic.edit import CreateView, UpdateView, DeleteView\nfrom django.core.urlresolvers import reverse_lazy, reverse\n'
        for model in models:
            string += '\n'
            string += 'from .models import ' + str(model['model'])
        for model in models:
            #CreateView generator
            string += '\n\n'
            string += '#Create view for ' + str(model['model']) + ' model.\n'
            string += 'class ' + str(model['model']) + 'CreateView' + '(CreateView):'
            string += '\n\ttemplate_name=' + "'" + '.html' + "'"
            string += '\n\tmodel=' + str(model['model'])
            string += '\n\tfields=['
            last = len(model['elements']) - 1
            for i, element in enumerate(model['elements']):
                string += "'" + element.name + "'"
                if i == last:
                    string += ']'
                else:
                    string += ', '
            string += '\n\tsuccess_url=reverse_lazy(' + "'" + "'" + ")"

            # UpdateView generator
            string += '\n\n'
            string += '#Update view for ' + str(model['model']) + ' model.\n'
            string += 'class ' + str(model['model']) + 'UpdateView' + '(UpdateView):'
            string += '\n\ttemplate_name=' + "'" + '.html' + "'"
            string += '\n\tmodel=' + str(model['model'])
            string += '\n\tfields=['
            last = len(model['elements']) - 1
            for i, element in enumerate(model['elements']):
                string += "'" + element.name + "'"
                if i == last:
                    string += ']'
                else:
                    string += ', '

            # DeleteView generator
            string += '\n\n'
            string += '#Delete view for ' + str(model['model']) + ' model.\n'
            string += 'class ' + str(model['model']) + 'DeleteView' + '(DeleteView):'
            string += '\n\ttemplate_name=' + "'" + '.html' + "'"
            string += '\n\tmodel=' + str(model['model'])
            string += '\n\tsuccess_url=reverse_lazy(' + "'" + "'" + ")"

            # ListView generator
            string += '\n\n'
            string += '#List view for ' + str(model['model']) + ' model.\n'
            string += 'class ' + str(model['model']) + 'ListView' + '(generic.ListView):'
            string += '\n\ttemplate_name=' + "'" + '.html' + "'"
            string += '\n\tcontext_object_name=' + "'" + 'all_' + str(model['model']) + "'"
            string += '\n\tdef get_queryset(self):'
            string += '\n\t\treturn ' + str(model['model']) + '.object.all'

        return string

    with open('C:/Users/Johny/Desktop/mrk/mysite/myapp/views.py', 'w') as f:
        a = test2(models1)
        f.write(a)

    def test3(models):
        string = 'kkk'
        return string

    with open('C:/Users/Johny/Desktop/mrk/mysite/myapp/urls.py', 'w') as f:
        a = test3(models1)
        f.write(a)


    def test4(models):
        string = 'from django.contrib import admin\nfrom .models import '
        last = len(models) - 1
        for i, model in enumerate(models):
            string += str(model['model'])
            if i == last:
                string += '' + '\n'
            else:
                string += ', '
        for model in models:
            string += '\n'
            string += 'admin.site.register(' + str(model['model']) + ')'

        return string

    with open('C:/Users/Johny/Desktop/mrk/mysite/myapp/admin.py', 'w') as f:
        a = test4(models1)
        f.write(a)
