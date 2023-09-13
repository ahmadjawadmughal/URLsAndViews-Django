from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def home(request):

    text = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home Page</title>
  </head>
  <body>
    <h1 style="color:blue;text-align:center;">Welcome to Ecom Site!</h1>
  </body>
</html>
"""

    return HttpResponse(text, content_type="text/html")

def about(request):
    
    text = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About</title>
  </head>
  <body>
    <h1 style="color:blue;text-align:center;">About Us</h1>
    <div>
    <h2>Detail</h2>
    <p>It is an Ecommerce app.</p>
    </div>
    <div>
    <h2>Purpose</h2>
    <p>Our purpose is to serve customers across the boundaries.</p>
    </div>
  </body>
</html>
"""    
    return HttpResponse(text, content_type="text/html")

def user_profile(request,username):

    text=f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>User Profile</title>
  </head>
  <body>
    <h1 style="color:blue;text-align:center;">Profile of {username}</h1>
    <div style="font-size:xx-large;">
    <p>{username} email: example@mail.com</p>
    <p>{username} password: ********</p>
    <p>{username} accounts details</p>
    </div>
  </body>
</html>   
"""

    return HttpResponse(text, content_type="text/html")    


# Redirect

def profile_redirect(request,username="AJM!"):

    return redirect (reverse("user_profile", kwargs={'username':username}))
    #return redirect(user_profile,username)