from django.conf.urls import url
from .views import HomeView, CategoryDetail, PostDetail

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='post_detail'),
]
