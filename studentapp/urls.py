from django.urls import path
from . import views
app_name = "studentapp"
urlpatterns = [
    path("home/",views.home,name="home"),
    path("apply/",views.application,name="apply"),
    path("dept/",views.dept,name="dept"),
    path("ece/",views.ece,name="ece"),
    path("eee/",views.eee,name="eee"),
    path("cse/",views.cse,name="cse"),
]
