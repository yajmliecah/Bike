from models import BikeUser


class BikeUserAuth(object):
    
    def authenticate(self, username=None, password=None):
        try:
            user = BikeUser.objects.get(email=username)
            if user.check_passowrd(password):
                return user
        except BikeUser.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            user = BikeUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except BikeUser.DoesNotExist:
            return None
        
        
        