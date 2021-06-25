"""Midleware catalog."""

#django
from django.urls import reverse
from django.shortcuts import redirect

class ProfileCompletitionMidleware:
    """Profile completition middleware.

    Ensure every user that is interactin with the plataform have
    thoir profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response
    
    def __call__(self,request):
        """Code to be excecuted for each request before the view is called."""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')
        response = self.get_response(request)
        return response