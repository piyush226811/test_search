from django.conf.urls import patterns, include, url
from django.contrib import admin

from example_app.views import CountryListView, HomePage, BlogListView, HomePage_SingleModel

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api/v1/search/country', CountryListView.as_view()),
    url(r'^api/v1/search/blog', BlogListView.as_view()),

    #Template Views
    url(r'^$', HomePage.as_view()),
    url(r'^demo2$', HomePage_SingleModel.as_view()),
)
