from .models import BeelineUser


class PhoneNumberAuthBackend():
    def authenticate(self, request, username, password):
        try:
            user = BeelineUser.objects.get(phone_number=username)
            if user.check_password(password):
                return user
            return None
        except BeelineUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return BeelineUser.objects.get(pk=user_id)
        except BeelineUser.DoesNotExist:
            return None
