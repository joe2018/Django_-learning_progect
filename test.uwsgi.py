 1 #coding:utf-8
 2 import os
 3 import sys
 4 reload(sys)
 5 sys.setdefaultencoding('utf8')
 6 
 7 from django.core.wsgi import get_wsgi_application
 8 
 9 os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")    #project为项目名，请按需求修改
10 
11 application = get_wsgi_application()
