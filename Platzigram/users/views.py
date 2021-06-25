"""Users views."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    """Login view.

    Args:
        request (request): request data
    Returns:
        HttpResponse: render users/login.hrml
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #print(username,password)
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request,'users/login.html')
    
@login_required
def logout_view(request):
    """logout user.

    Args:
        request

    Returns:
        redirect to login
    """
    logout(request)
    return redirect('login')

def signup_view(request):
    """Dignup view."""
    return render(request,'users/signup.html')