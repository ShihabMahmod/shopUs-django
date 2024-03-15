from django.urls import path
from home.views import index,about,contact_us,blogs,blog,terms,error

urlpatterns = [
   
    path('' , index , name="index"),
    path('about',about , name="about"),
    path('contact-us', contact_us, name="contact_us"),
    path('blogs', blogs, name="blogs"),
    path('blog', blog, name="blog"),
    path('terms', terms, name="terms"),
    path('400', error, name="error")
]
