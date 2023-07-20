from django.contrib import admin
from django.urls import path, include
from api.views import intj_api_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', intj_api_view, name='intj_api'),
    path('', include('profiles.urls')),  # Include the profiles app's URLs under the 'profiles/' prefix
]
