from django.contrib.auth.backends import ModelBackend

from base.models import User

class CustomerBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        n = kwargs['username']
        passw = kwargs['password']
        try:
            customer = User.objects.get(name=n)
            if customer.name==n and customer.password==passw:
                return customer
        except User.DoesNotExist:
            pass