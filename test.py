import os


os.popen('git bisect start $eed312912caa4f78c2b946faf2b21720d34e3888 $ff0c9dcc5d11fbbdcebe681dda56ff34798344e8')
os.popen('cd budgetproject && python manage.py test budget && cd ..')