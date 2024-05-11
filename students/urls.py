from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # /admin/*/
    path('admin/', admin.site.urls),
    # /*/
    path('', include('pupil.urls')),
    # /room/*/
    path('room/', include('studentroom.urls'))
]
