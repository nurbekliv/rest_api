from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Parents, Children, WorkHistory, Educations
from .serializers import ParentsSerializer, ChildrenSerializer, WorkHistorySerializer, EducationsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ParentsViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ['f_number', 'm_number']
    search_fields = ['address']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('f_number', openapi.IN_QUERY, description="Filter by father's number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('m_number', openapi.IN_QUERY, description="Filter by mother's number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('search', openapi.IN_QUERY, description="Search by address", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ['ch_number', 'family_id']
    search_fields = ['first_name', 'last_name']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('ch_number', openapi.IN_QUERY, description="Filter by child's number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('family', openapi.IN_QUERY, description="Filter by family (parent's ID)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('first_name', openapi.IN_QUERY, description="Filter by birth date", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        openapi.Parameter('last_name', openapi.IN_QUERY, description="Search by first name or last name", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ['work_number']
    search_fields = ['company']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('work_number', openapi.IN_QUERY, description="Filter by child's number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('company', openapi.IN_QUERY, description="Search by first name or last name", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EducationsViewSet(viewsets.ModelViewSet):
    queryset = Educations.objects.all()
    serializer_class = EducationsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ['education_number']
    search_fields = ['name']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('education_number', openapi.IN_QUERY, description="Filter by child's number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('name', openapi.IN_QUERY, description="Search by first name or last name", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
