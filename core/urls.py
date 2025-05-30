from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API Router
router = DefaultRouter()
router.register(r'plants', views.PlantViewSet)
router.register(r'categories', views.ProductCategoryViewSet)
router.register(r'sku-clusters', views.SkuClusterViewSet)
router.register(r'production-lines', views.ProductionLineViewSet)
router.register(r'machines', views.MachineViewSet)
router.register(r'monthly-plans', views.MonthlyPlanViewSet)
router.register(r'weekly-schedules', views.WeeklyScheduleViewSet)
router.register(r'machine-schedules', views.MachineScheduleViewSet)
router.register(r'production-kpis', views.ProductionKpiViewSet)

urlpatterns = [
    # Frontend routes
    path('', views.dashboard_view, name='dashboard'),
    path('monthly-planning/', views.monthly_planning_view, name='monthly-planning'),
    path('weekly-schedule/', views.weekly_schedule_view, name='weekly-schedule'),
    path('machine-planning/', views.machine_planning_view, name='machine-planning'),
    path('reports/', views.reports_view, name='reports'),
    path('login/', views.login_view, name='login'),
    
    # API routes
    path('api/', include(router.urls)),
    path('api/sap-integration/refresh/', views.sap_integration_refresh, name='sap-refresh'),
    path('api/machines/<int:machine_id>/status/', views.update_machine_status, name='update-machine-status'),
]