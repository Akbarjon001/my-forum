from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView),
    path('create', views.CreateTopicView),
    path('topics', views.ForumView),
    path('topics/<int:topic_id>', views.TopicView),
    path('categories', views.CategoriesView),
    path('categories/<str:type_category>', views.CategoryView),
    path('contact', views.ContactView)
]