from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register),
    path('login', views.kidlogin),
    path('selectcategory', views.selectcategory),
    path('selecttopic/<int:category_id>', views.selecttopic),
    path('selectquiz/<int:topic_id>', views.selectquiz),
    path('takequiz/<int:quiz_id>', views.takequiz),
    path('processquiz/<int:quiz_id>', views.processquiz),
    path('results/<int:quiz_id>', views.results),
    path('logout', views.logout),
]