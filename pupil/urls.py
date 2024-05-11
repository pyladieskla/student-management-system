from django.urls import path
from .views import index, test, get_outer_template, get_inner_template


urlpatterns = [
    # /
    path('', index),
    # /home/
    path('home', index),
    # /test/{any_number}/
    path('test/<int:id>/', test, name="test"),
    # /outer/
    path('outer', get_outer_template, name="outer"),
    # /inner/
    path('inner', get_inner_template, name="inner"),

    # /{pupil_id}
    # path('<int:pupil_id>/', view_pupil, name="view_pupil")

]
