from django.urls import path
from .views import homePageView, registerFlight, listFlight, statsFlights

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path("register/", registerFlight.as_view(), name="register"),
    path("list/", listFlight.as_view(), name="list"),
     path("stats/", statsFlights.as_view(), name="stats"),

]
