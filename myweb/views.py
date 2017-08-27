# -*- coding=utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import time
from django.http import HttpResponseRedirect




# Create your views here.

# def hello(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'hello.html', context)

# def game(request):
#     context = {}
#     cursor = connection.cursor()
#     sql = "SELECT * FROM `game_test`"
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获取所有记录列表
#         results = cursor.fetchall()
#         result = []
#         for i in results:
#             result.append(i)
#
#         context['hello'] = result
#     except:
#         context['hello'] = '空'
#     return render(request, 'hello.html', context)


def plan(request):
    context = {}
    Data = []
    cursor = connection.cursor()
    sql = "SELECT `ID`,`JIEDUAN`,`NEIRONG`,`SHUOMING`,`WCQK`,`GXSJ` FROM `plan_mh`"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            result = {}
            result['id'] = row[0]
            result['jieduan'] = row[1]
            result['neirong'] = row[2]
            result['shuoming'] = row[3]
            result['wangcheng'] = row[4]
            result['gengxin'] = row[5]
            Data.append(result)
        context['plan'] = Data
    except:
        context['plan'] = '错误'
    return render(request, 'plan.html', context)


def receive_data(request):
    getUserName = request.GET.get('id')
    print(getUserName)
    if request.POST:  # 如果数据提交
        print('有提交')
        # select = request.POST.get('select', None)
        text = request.POST.get('text', None)
        cursor = connection.cursor()
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(now_time)
        if text == '完成':
            sql = 'UPDATE `plan_mh` SET `WCQK` = "完成",`GXSJ` = "%s" WHERE `plan_mh`.`ID` = %s'
            cursor.execute(sql % (str(now_time),getUserName))
        else:
            sql = 'UPDATE `plan_mh` SET `WCQK` = "未完成" ,`GXSJ` = "%s" WHERE `plan_mh`.`ID` = %s'
            cursor.execute(sql % (str(now_time),getUserName))
        print(text)
        print(locals())
    return render(request, 'hello.html', locals())


