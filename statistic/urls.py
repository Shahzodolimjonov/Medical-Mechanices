from django.urls import path
from .views import EmployeeStatistics, AllEmployeesStatistics, ClientStatistics, EmployeeAPIView, ClientAPIView, \
    ProductAPIView, OrderAPIView, OrderViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("EmployeeAPIView/", EmployeeAPIView.as_view(), name='list'),
    path("ClientAPIView/", ClientAPIView.as_view(), name='client'),
    path("ProductAPIView/", ProductAPIView.as_view(), name='product'),
    path("OrderAPIView/", OrderAPIView.as_view(), name='order'),
    path('statistics/employee/<int:pk>/', EmployeeStatistics.as_view(), name='employee_statistics'),
    path('employee/statistics/', AllEmployeesStatistics.as_view(), name='all_employees_statistics'),
    path('statistics/client/<int:pk>/', ClientStatistics.as_view(), name='client_statistics'),

]

router = SimpleRouter()
router.register("", OrderViewSet, basename='post')
urlpatterns += router.urls
