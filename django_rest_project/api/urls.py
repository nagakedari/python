from django.urls import path
from django.urls.conf import include
from api.views import BlogApi
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from api import views
from django.conf.urls.static import static
from django.conf import settings

app_name='api'

urlpatterns = [
    url('blog', BlogApi.as_view(), name='blog'),
    url('blog/<int:pk>', BlogApi.as_view(), name='blog_details'),
    # path('save_post', api_save_blog_view, name='blog_post'),
    url(r'^departments$',views.departmentapi),
    url(r'^departments/([0-9]+$)', views.departmentapi),
    url(r'^employees$',views.employeeapi),
    url(r'^employees/([0-9]+$)', views.employeeapi),
    url(r'^save_file', views.save_image)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = format_suffix_patterns(urlpatterns)