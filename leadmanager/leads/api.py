from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# A viewset allows us to create full CRUD APIs without declaring explicit methods, (ex: POST, GET, etc)
# Lead View set
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
