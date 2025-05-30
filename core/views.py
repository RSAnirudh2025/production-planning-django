from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
import json
from datetime import datetime, date

# Frontend Views
def dashboard_view(request):
    return render(request, 'dashboard.html')

def monthly_planning_view(request):
    return render(request, 'monthly-planning.html')

def weekly_schedule_view(request):
    return render(request, 'weekly-schedule.html')

def machine_planning_view(request):
    return render(request, 'machine-planning.html')

def reports_view(request):
    return render(request, 'reports.html')

def login_view(request):
    return render(request, 'login.html')

# API ViewSets
class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class SkuClusterViewSet(viewsets.ModelViewSet):
    queryset = SkuCluster.objects.all()
    serializer_class = SkuClusterSerializer

class ProductionLineViewSet(viewsets.ModelViewSet):
    queryset = ProductionLine.objects.all()
    serializer_class = ProductionLineSerializer

    def get_queryset(self):
        queryset = ProductionLine.objects.all()
        plant_id = self.request.query_params.get('plant_id', None)
        if plant_id is not None:
            queryset = queryset.filter(plant__id=plant_id)
        return queryset

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get_queryset(self):
        queryset = Machine.objects.all()
        line_id = self.request.query_params.get('line_id', None)
        if line_id is not None:
            queryset = queryset.filter(line__id=line_id)
        return queryset

class MonthlyPlanViewSet(viewsets.ModelViewSet):
    queryset = MonthlyPlan.objects.all()
    serializer_class = MonthlyPlanSerializer

    def get_queryset(self):
        queryset = MonthlyPlan.objects.all()
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        if month is not None and year is not None:
            queryset = queryset.filter(month=month, year=year)
        return queryset

class WeeklyScheduleViewSet(viewsets.ModelViewSet):
    queryset = WeeklySchedule.objects.all()
    serializer_class = WeeklyScheduleSerializer

    def get_queryset(self):
        queryset = WeeklySchedule.objects.all()
        week_number = self.request.query_params.get('week_number', None)
        year = self.request.query_params.get('year', None)
        plant_id = self.request.query_params.get('plant_id', None)
        
        if week_number is not None and year is not None:
            queryset = queryset.filter(week_number=week_number, year=year)
        if plant_id is not None:
            queryset = queryset.filter(plant__id=plant_id)
        return queryset

class MachineScheduleViewSet(viewsets.ModelViewSet):
    queryset = MachineSchedule.objects.all()
    serializer_class = MachineScheduleSerializer

    def get_queryset(self):
        queryset = MachineSchedule.objects.all()
        machine_id = self.request.query_params.get('machine_id', None)
        date_param = self.request.query_params.get('date', None)
        
        if machine_id is not None:
            queryset = queryset.filter(machine__id=machine_id)
        if date_param is not None:
            queryset = queryset.filter(date=date_param)
        return queryset

class ProductionKpiViewSet(viewsets.ModelViewSet):
    queryset = ProductionKpi.objects.all()
    serializer_class = ProductionKpiSerializer

    def get_queryset(self):
        queryset = ProductionKpi.objects.all()
        date_param = self.request.query_params.get('date', None)
        plant_id = self.request.query_params.get('plant_id', None)
        
        if date_param is not None:
            queryset = queryset.filter(date=date_param)
        if plant_id is not None:
            queryset = queryset.filter(plant__id=plant_id)
        return queryset

@api_view(['POST'])
def sap_integration_refresh(request):
    # Simulate SAP refresh
    return Response({
        'success': True,
        'message': 'SAP data refreshed successfully',
        'timestamp': datetime.now().isoformat()
    })

@api_view(['PATCH'])
def update_machine_status(request, machine_id):
    try:
        machine = Machine.objects.get(id=machine_id)
        status = request.data.get('status')
        if status in dict(Machine.STATUS_CHOICES):
            machine.status = status
            machine.save()
            serializer = MachineSerializer(machine)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
    except Machine.DoesNotExist:
        return Response({'error': 'Machine not found'}, status=status.HTTP_404_NOT_FOUND)