from django.core.exceptions import PermissionDenied

def superuser_check(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request)
        else:
            raise PermissionDenied("You are not eligible to add products in the shop")
    return wrapper