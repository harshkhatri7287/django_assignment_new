from django.shortcuts import redirect

EXEMPT_URLS = [
    '/signin/',
    '/signup/',
    '/changepassword/',
]

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (not request.user.is_authenticated) and (request.path not in EXEMPT_URLS):
            return redirect('signin')
        return self.get_response(request)
