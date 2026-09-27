from django.urls import path
from . import views
urlpatterns=[
 path('register/',views.register_visitor,name='register_visitor'),
 path('my-visitors/',views.student_visitors,name='student_visitors'),
 path('warden/',views.warden_requests,name='warden_requests'),
 path('warden/<int:pk>/<str:status>/',views.update_status,name='update_status'),
 path('security/',views.security,name='security'),
 path('security/entry/<int:pk>/',views.entry,name='entry'),
 path('security/exit/<int:pk>/',views.exit,name='exit'),
]
