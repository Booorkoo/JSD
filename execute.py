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
                        string += 'max_length=' + element.datatype.textfield.parameters[1].max_length.number + ")), "

                    elif element.datatype.textfield.parameters[0].max_length and element.datatype.textfield.parameters[1].default is not None:
                        string += 'max_length=' + element.datatype.textfield.parameters[0].max_length.number + ", "
                        string += 'default=' + element.datatype.textfield.parameters[1].default.number + ")),"

                    elif element.datatype.textfield.parameters[0].default and element.datatype.textfield.parameters[1].max_length is not None:
                        string += 'default=' + element.datatype.textfield.parameters[0].default.number + ", "
                        string += 'max_length=' + element.datatype.textfield.parameters[1].max_length.number + ")),"

                    elif element.datatype.textfield.parameters[0].null and element.datatype.textfield.parameters[1].default is not None:
                        string += 'null=' + element.datatype.textfield.parameters[0].null.value + ","
                        string += 'default=' + element.datatype.textfield.parameters[1].default.number + ")), "

                    elif element.datatype.textfield.parameters[0].default and element.datatype.textfield.parameters[1].null is not None:
                        string += 'default=' + element.datatype.textfield.parameters[0].default.number + ", "
                        string += 'null=' + element.datatype.textfield.parameters[1].null.value + ")),"




            string += '\n\t\t\t],'
            string += '\n\t\t),'
        string += '\n\t]'
        return string


    with open('C:/Users/Johny/Desktop/jsd/jsd/0001_initial.py', 'w') as f:
        a = test(models1)
        f.write(a)

