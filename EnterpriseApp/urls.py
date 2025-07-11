
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('accounts/', include('accounts.urls')),
    path('leaves/', include('leave_requests.urls')),
    path('policies/', include('policies.urls')),
    path('trainings/', include('trainings.urls')),
    path('contacts/', include('departments.urls')),
]

