from django.db import models

# Create your models here.


# 用户
class User(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    loginDate = models.DateField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)


# files
class Files(models.Model):
    # 任务id
    task_id = models.CharField(max_length=50)
    # 源文件路径以及名字
    source_file_path = models.CharField(max_length=100)
    # 需要添加的功能
    timestamp = models.BooleanField(default=False)
    # 任务状态 -1上传本地服务器成功
    status = models.IntegerField(default=-1)
    # 失败原因
    failure_reason = models.CharField(max_length=100)
    # json文件路径
    json_file_path = models.CharField(max_length=100)
    # 目标文件  带时间戳  和  全文本
    objectFile_Timestamp_Path = models.CharField(max_length=100)
    objectFile_Contend_path = models.CharField(max_length=100)
    # 时间
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(blank=True, null=True)
    # 下载次数
    download_num = models.IntegerField(default=0)
    # 外键  记录产生的用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
