#-*- coding: utf-8 -*-
from django.shortcuts import render

import os

from .models import Files, User

from jpype import *

import datetime

import time


# Create your views here.
def index(request):
    """主页"""
    # 两个参数：原始请求对象、可用于创建网页的模版
    return render(request, 'voice_transcriptions/index.html')


def trans_result(request):
    """结果页面"""
    # 两个参数：原始请求对象、可用于创建网页的模版
    return render(request, 'voice_transcriptions/trans_result.html')


# timestamp : 01
# analysis : 02
def upload_file(request):
    """上传文件以及选择增加的功能"""
    if request.method == 'POST':
        # 暂时先没写用户，所以统一用默认用户名
        user = User.objects.get(id=1)
        filelist = request.FILES.getlist('inputfile', None)
        # features 是一个list
        features = request.POST.getlist('features', None)
        timestamp = False
        if '01' in features:
            timestamp = True
        if not filelist:
            return render(request, 'voice_transcriptions/fail.html')
        for file in filelist:
            files_model = Files()
            file_path = handle_uploaded_file(file)
            files_model.source_file_path = file_path
            files_model.timestamp = timestamp
            files_model.user = user
            files_model.save()
            # 数据库操作完毕
        context = {'features': features}
        return render(request, 'voice_transcriptions/success.html', context)


def handle_uploaded_file(file):
    # 打开特定的文件进行二进制的写操作
    dir = "E:/vt_fileupload/"
    folder = os.path.exists(dir)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
        # makedirs 创建文件时如果路径不存在会创建这个路径
        os.makedirs(dir)
    path = os.path.join(dir, file.name)
    destination = open(path, 'wb+')
    # 分块写入文件
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return path


# 写好了但还没整合，尝试运行的时候记得注释掉这个函数
def processing_files(sourcepath, resultpath):
    """调用JPype实例化科大讯飞语音转写Java接口类"""
    # 连接到jar包
    jarpath = os.path.join(os.path.abspath('.'), 'D:/Workspace/lfasr-sdk/')
    startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath + 'lfasr-sdk_fat.jar'))
    # 初始化类
    base_infor_class = JClass('com.iflytek.msp.lfasr.BaseInfor')
    operation_class = JClass('com.iflytek.msp.lfasr.Operation')
    # 定义常量
    sleep_second = 20
    sourceFilePath = sourcepath
    resultFilePath = resultpath
    # 实例化非static方法
    BaseInforIns = base_infor_class(sourceFilePath, resultFilePath)
    base_infor_class.propertiesPath = "D:/Workspace/lfasr-sdk/log4j.properties"
    lc = operation_class.Register(BaseInforIns)
    # 执行转录过程
    if lc:
        if operation_class.uploadTask(lc, BaseInforIns) != 0:
            while True:
                if operation_class.getTaskStatus(base_infor_class.task_id, lc) != 0:
                    break
                    # 以秒数为单位，Java的sleep是以毫秒为单位
                time.sleep(sleep_second)
                print("waiting...")
            json_result = operation_class.getResult(base_infor_class.task_id, lc)
            print("json_result:"+json_result)
            if operation_class().writeFile(base_infor_class.jsonFilePathString, json_result):
                print("id = %s 结果已经写入json " % base_infor_class.task_id)
    shutdownJVM()


# def close_JVM():
#     """关闭Java虚拟机"""
#     shutdownJVM()


# 下面两个函数是用来测试的
def success(request):
    """成功页面"""
    return render(request, 'voice_transcriptions/success.html')


def fail(request):
    """失败页面"""
    return render(request, 'voice_transcriptions/fail.html')
