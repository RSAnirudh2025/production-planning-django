from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    manager = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Categories"

class SkuCluster(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.name}"

class ProductionLine(models.Model):
    name = models.CharField(max_length=255)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    efficiency_target = models.FloatField(default=85.0)

    def __str__(self):
        return f"{self.name} - {self.plant.name}"

class Machine(models.Model):
    STATUS_CHOICES = [
        ('operational', 'Operational'),
        ('maintenance', 'Maintenance'),
        ('breakdown', 'Breakdown'),
        ('idle', 'Idle'),
    ]
    
    name = models.CharField(max_length=255)
    line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='operational')

    def __str__(self):
        return f"{self.name} - {self.line.name}"

class MonthlyPlan(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    sku_cluster = models.ForeignKey(SkuCluster, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    planned_quantity = models.IntegerField()
    target_efficiency = models.FloatField(default=85.0)

    def __str__(self):
        return f"{self.sku_cluster.code} - {self.month}/{self.year}"

    class Meta:
        unique_together = ['month', 'year', 'sku_cluster', 'plant']

class WeeklySchedule(models.Model):
    week_number = models.IntegerField()
    year = models.IntegerField()
    sku_cluster = models.ForeignKey(SkuCluster, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    planned_quantity = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Week {self.week_number}/{self.year} - {self.sku_cluster.code}"

    class Meta:
        unique_together = ['week_number', 'year', 'sku_cluster', 'plant']

class MachineSchedule(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.CharField(max_length=20)
    sku_cluster = models.ForeignKey(SkuCluster, on_delete=models.CASCADE)
    planned_quantity = models.IntegerField()
    actual_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.machine.name} - {self.date} - {self.shift}"

    class Meta:
        unique_together = ['machine', 'date', 'shift']

class ProductionKpi(models.Model):
    date = models.DateField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)
    sku_cluster = models.ForeignKey(SkuCluster, on_delete=models.CASCADE, null=True, blank=True)
    planned_quantity = models.IntegerField()
    actual_quantity = models.IntegerField()
    efficiency = models.FloatField()
    downtime_minutes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.plant.name} - {self.date} - {self.efficiency}%"

    class Meta:
        verbose_name = "Production KPI"
        verbose_name_plural = "Production KPIs"