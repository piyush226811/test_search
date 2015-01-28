from django.db.models import Q
from django.views.generic import TemplateView
from rest_framework import generics

from .models import Country, Blog
from .serializer import CountrySerializer, BlogSerializer


class CountryListView(generics.ListAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        queryset = super(CountryListView, self).get_queryset()
        keyword = self.request.query_params.get('q', None)
        if keyword:
            queryset = queryset.filter(Q(name__icontains=keyword))
        return queryset


class BlogListView(generics.ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset()
        keyword = self.request.query_params.get('q', None)
        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(text__icontains=keyword))
        return queryset


class HomePage(TemplateView):

    template_name = 'demo.html'


class HomePage_SingleModel(TemplateView):

    template_name = 'demo2.html'


class HomePage_MultiColumn(TemplateView):

    template_name = 'demo3.html'
