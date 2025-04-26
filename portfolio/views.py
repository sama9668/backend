from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import UserSerializer, EducationSerializer, WorkSerializer, PortfolioSerializer
from .models import Education, Work, Portfolio



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows education records to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows work records to be viewed or edited.
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PortfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows portfolio items to be viewed or edited.
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
