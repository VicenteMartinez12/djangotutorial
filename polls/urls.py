from django.urls import path

from . import views


app_name = "polls"

# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     # path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
#     # added the word 'specifics'
#     path("specifics/<int:question_id>/", views.detail, name="detail"),
    
# ]

from django.urls import path,include

from . import views
from .views import service_worker
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
  path('', include('pwa.urls')),
path('serviceworker.js', service_worker, name='service-worker'),
]