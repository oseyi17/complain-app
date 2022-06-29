
from django.urls import path
from .views import HomePageView, ComplainView, thanks, DetailPageView, DeletePageView, bug, dashboard

urlpatterns=[
    path('', ComplainView.as_view(), name='complain'),
    path('thanks/', thanks, name='thanks'),
    path('list/', HomePageView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name='detail'),
    path('complain/<int:pk>/delete', DeletePageView.as_view(), name='delete'),
    path('bug/report/', bug.as_view(), name='bug_report'),
    path('dashboard', dashboard, name='dashboard'),
]

