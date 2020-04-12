"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from .views import ListVideo, VideoDetail
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('', ListVideo.as_view(), name="lista-videos" ),
    path('<pk>', VideoDetail.as_view(), name="single-video" ),
]


# (?P<pk>[0-9]+)

# path('videos/', ListVideo.as_view(), name="lista-videos" ),
# url(r'^videos/', include('rest_framework.urls', namespace='lista-videos')),
# url(r'^videos/', ListVideo.as_view(), include('rest_framework.urls', namespace='lista-videos')),