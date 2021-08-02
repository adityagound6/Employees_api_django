#from employee.viewset import EmployeeViewSet
from rest_framework import routers
from employee.viewSet import EmployeeViewSet


router = routers.DefaultRouter()
router.register('employee',EmployeeViewSet)