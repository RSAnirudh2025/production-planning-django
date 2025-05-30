from rest_framework import serializers
from .models import *

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class SkuClusterSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = SkuCluster
        fields = '__all__'

class ProductionLineSerializer(serializers.ModelSerializer):
    plant_name = serializers.CharField(source='plant.name', read_only=True)
    
    class Meta:
        model = ProductionLine
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    line_name = serializers.CharField(source='line.name', read_only=True)
    plant_name = serializers.CharField(source='line.plant.name', read_only=True)
    
    class Meta:
        model = Machine
        fields = '__all__'

class MonthlyPlanSerializer(serializers.ModelSerializer):
    sku_cluster_code = serializers.CharField(source='sku_cluster.code', read_only=True)
    sku_cluster_name = serializers.CharField(source='sku_cluster.name', read_only=True)
    plant_name = serializers.CharField(source='plant.name', read_only=True)
    
    class Meta:
        model = MonthlyPlan
        fields = '__all__'

class WeeklyScheduleSerializer(serializers.ModelSerializer):
    sku_cluster_code = serializers.CharField(source='sku_cluster.code', read_only=True)
    sku_cluster_name = serializers.CharField(source='sku_cluster.name', read_only=True)
    plant_name = serializers.CharField(source='plant.name', read_only=True)
    
    class Meta:
        model = WeeklySchedule
        fields = '__all__'

class MachineScheduleSerializer(serializers.ModelSerializer):
    machine_name = serializers.CharField(source='machine.name', read_only=True)
    sku_cluster_code = serializers.CharField(source='sku_cluster.code', read_only=True)
    
    class Meta:
        model = MachineSchedule
        fields = '__all__'

class ProductionKpiSerializer(serializers.ModelSerializer):
    plant_name = serializers.CharField(source='plant.name', read_only=True)
    machine_name = serializers.CharField(source='machine.name', read_only=True)
    sku_cluster_code = serializers.CharField(source='sku_cluster.code', read_only=True)
    
    class Meta:
        model = ProductionKpi
        fields = '__all__'