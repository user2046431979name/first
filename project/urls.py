from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import * 
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',SignUp.as_view(),name='signup'),
    path('',index,name='index'),
    path('single/<int:id>', single, name='single'),
    path('about/',about),
    path('like/',likes,name='like'),
    path('comment/<int:id>',comments,name='coments'),
    
]


urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
