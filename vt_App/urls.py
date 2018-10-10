"""定义voice_transcriptions的URL模式"""

# 导入函数url，使用它来将URL映射到视图
from django.urls import path
# 导入模块views，句点表示让Python从当前的urls.py模块所在的文件夹中导入视图
from . import views
# urlpatterns是列表，包含可在应用程序learning_logs中请求的网页
urlpatterns = [
    # 主页
    path('', views.index, name="index"),
    # 结果页面
    path('trans_result/', views.trans_result, name="trans_result"),
    # 上传文件的页面
    path('upload_file/', views.upload_file, name="upload_file"),
    # 成功页面
    path('success/', views.success, name="success"),
    # 失败页面
    path('fail/', views.fail, name="fail"),
]