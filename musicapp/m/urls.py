from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'),
    path('mlist/', views.mlist, name='mlist'),
    path('mdeta/', views.mdeta, name='mdeta'),
    path('play/', views.play, name='play'),
  
    ]



urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)