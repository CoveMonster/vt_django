"""vt_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 导入函数url，使用它来将URL映射到视图
from django.urls import path
# 导入模块views，句点表示让Python从当前的urls.py模块所在的文件夹中导入视图
from django.urls import path, include
# urlpatterns是列表，包含可在应用程序learning_logs中请求的网页

urlpatterns = [
    path('admin/', admin.site.urls),
    # 我们需要包含voice_transcriptions的URL,
    # 包含namespace让我们能够将voice_transcriptions中的URL同项目中的其他URL区分开来，在项目扩展时很有帮助
    path('vt_App/', include(('vt_App.urls', 'vt_App'),
                                          namespace='voice_transcriptions')),
]
