from django.contrib import admin
from django.db import router
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename="Student")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

 #   path('stuinfo/',views.student_api),
 #   path('stuinfo/<int:pk>',views.student_api),

 #    path('stuinfo/',views.StudentLC.as_view()),
 #    path('stuinfo/<int:pk>',views.StudentRUD.as_view()),

 #     path('stuinfo/',views.StudentListCreate.as_view()),
 #     path('stuinfo/<int:pk>',views.StudentRetUpdDes.as_view()),
]
