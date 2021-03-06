from django.urls import path
from . import views

urlpatterns = [
    path('',  views.homePage, name = 'home'), 
    path('about/',  views.aboutPage, name = 'about'), 
    path('contact/',  views.contactPage, name = 'contact'), 
    path('blog/', views.blogView.as_view(), name='blog'),
    path('blog/post/<int:pk>', views.postDetailView.as_view(), name='blog_post'),
    path('blog/add_post/', views.addPostView.as_view(), name='add_post'),
    path('blog/edit_post/<int:pk>', views.editPostView.as_view(), name='edit_post'),
    path('blog/<int:pk>/delete', views.deletePostView.as_view(), name='delete_post'),
    path('blog/category/', views.blogCatsView.as_view(), name='blog_cats'),
    path('blog/category/<str:categories>/', views.categoryView, name='category'),
    path('careers/',  views.careersView.as_view(), name = 'careers'),
    path('careers/<int:pk>', views.careersDetailView.as_view(), name = 'careers_post'),
    path('register/', views.userRegisterView.as_view(), name='register'),
]
