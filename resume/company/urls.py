from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='company'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<c_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<a_id>[0-9]+)/app_detail/$', views.app_detail, name='app_detail'),
    url(r'add_company/$', views.AddCompany, name="add_company"),
    url(r'add_company_sub/$', views.AddCompanySub, name="add_company_sub"),

    url(r'(?P<p_id>[0-9]+)/add_application/$', views.AddApplication, name="add_application"),
    url(r'add_application_sub/$', views.AddApplicationSub, name="add_application_sub"),
    #url(r'^(?P<a_id>[0-9]+)/external_link/$', views.external_view, name='external_view'),
    #url(r'$', views.Home.as_view(), name='Home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
