from django.urls import path

from reviews.apps import ReviewsConfig
from users.urls import app_name, urlpatterns

app_name = ReviewsConfig.name

urlpatterns = [

]