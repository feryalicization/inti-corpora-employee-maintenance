from rest_framework import generics
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied




class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"detail": "Permission denied. Only admin members can create users."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]  

    def perform_create(self, serializer):
        # Check if the requesting user is staff
        if not self.request.user.is_staff:
            raise PermissionDenied("Permission denied. Only admin members can create employees.")
        serializer.save()

    def list(self, request, *args, **kwargs):
        # Check if the requesting user is staff
        if not self.request.user.is_staff:
            raise PermissionDenied("Permission denied. Only admin members can view the list of employees.")
        return super().list(request, *args, **kwargs)

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Check if the requesting user is staff
        if not self.request.user.is_staff:
            raise PermissionDenied("Permission denied. Only admin members can update employees.")
        serializer.save()

    def perform_destroy(self, instance):
        # Check if the requesting user is staff
        if not self.request.user.is_staff:
            raise PermissionDenied("Permission denied. Only admin members can delete employees.")
        instance.delete()

    def retrieve(self, request, *args, **kwargs):
        # Check if the requesting user is staff
        if not self.request.user.is_staff:
            raise PermissionDenied("Permission denied. Only admin members can view employee details.")
        return super().retrieve(request, *args, **kwargs)