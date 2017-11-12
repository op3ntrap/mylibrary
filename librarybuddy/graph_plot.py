"""
@author=op3ntrap@gmail.com
Plot Model Graphs Using django-extensions graph_models command. base command
"graph_models --layout circo APP_NAME --pydot --group-models --verbose-names"
"""
from django.apps import apps
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
print(os.environ)
# import pydot

# app_names = [n for n in list(apps.app_configs) if "Manager" in n]
# print(app_names)
# app_names = ['UserManager', 'BookManager', 'TransactionManager', 'AlertManager', 'AnalyticsManager']
# for app in app_names:
# 	base_command = "graph_models --layout circo {} --pydot --group-models --verbose-names > {}.dot".format(app, app)
# 	python_command = "python manage.py "
# 	print(python_command+ base_command)
# 	os.system(python_command + base_command)
# graph, = pydot.graph_from_dot_file('{}.dot'.format(app))
# graph.write_png('{}.png'.format(app))
# print("{} has been export as png successfully".format(app))
modls = ['UserManager' + ' --include-models ' + 'Membership',
         'UserManager' + ' --include-models ' + 'Member',
         'UserManager' + ' --include-models ' + 'Librarian',
         'BookManager' + ' --include-models ' + 'DigitalRecords',
         'BookManager' + ' --include-models ' + 'Book',
         'BookManager' + ' --include-models ' + 'Magazine',
         'BookManager' + ' --include-models ' + 'Journal',
         'BookManager' + ' --include-models ' + 'ResearchPaper',
         'TransactionManager' + ' --include-models ' + 'Returning',
         'TransactionManager' + ' --include-models ' + 'Lend',
         'AlertManager' + ' --include-models ' + 'EmailAlerts',
         'AlertManager' + ' --include-models ' + 'EmailClient']
for app in modls:
	base_command = "graph_models {} --layout circo --pydot --verbose-names > {}.dot".format(app, app.split(' ')[2])
	python_command = "python manage.py "
	print(python_command + base_command)
	os.system(python_command + base_command)

for app in modls:
	graph, = pydot.graph_from_dot_file('{}.dot'.format(app.split(' ')[2]))
	graph.write_png('{}.png'.format(app))
	print("{} has been export as png successfully".format(app.split(' ')[2]))
