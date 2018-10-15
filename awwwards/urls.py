
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(?P<user_id>\d+)?$', views.profile, name='profile'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

