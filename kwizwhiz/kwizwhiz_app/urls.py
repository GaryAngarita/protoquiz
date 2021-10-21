from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about', views.about),
    path('contact', views.contact),
    path('media', views.media),
    path('recommend', views.recommend),
    path('logreg', views.logreg),
    path('register', views.register),
    path('login', views.login),
    # path('updateaccount/<user_id>', views.updateaccount),
    path('selectcategory', views.selectcategory),
    path('selecttopic/<int:category_id>', views.selecttopic),
    path('selectquiz/<int:topic_id>', views.selectquiz),
    path('takequiz/<int:quiz_id>', views.takequiz),
    path('processquiz/<int:quiz_id>', views.processquiz),
    path('results/<int:quiz_id>', views.results),
    path('logout', views.logout),
]