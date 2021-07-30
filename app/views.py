from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Provider, Coordinate, ServiceArea
from app.serializers import ProviderSerializer, ServiceAreaSerializer, CoordinateSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny]


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.AllowAny]


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
    permission_classes = [permissions.AllowAny]


class ServiceAreasByProviderViewSet(APIView):
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        provider_id = self.request.query_params.get('provider_id')
        data = []

        for service_area in ServiceArea.objects.filter(provider=provider_id):
            data.append(ServiceAreaSerializer(service_area).data)

        return Response(data)


class CoordinatesByServiceArea(APIView):
    serializer_class = CoordinateSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        service_area_id = self.request.query_params.get('service_area_id')
        data = []

        for coordinate in Coordinate.objects.filter(service_area=service_area_id):
            data.append(CoordinateSerializer(coordinate).data)

        return Response(data)
