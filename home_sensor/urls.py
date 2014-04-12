from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from api import views

admin.autodiscover()

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'sensor-nodes', views.SensorNodeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home_sensor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
