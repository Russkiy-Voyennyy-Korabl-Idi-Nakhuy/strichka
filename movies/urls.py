from django.conf.urls import url

from movies.views import TestView

urlpatterns = [url("", view=TestView.as_view(), name="index")]
