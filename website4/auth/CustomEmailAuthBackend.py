from django.contrib.auth.models import User

class EmailAuthBackend():
    def authenticate(request,self,username,password):
        try:
            user=User.objects.get(email=username)
            success=user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None
    def get_user(self,uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None
