from django.contrib.auth.base_user import BaseUserManager
class UserManger(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(("Phone Number is Requiredd"))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        # # extra_fields.setdefault('is_admin', True)
        # print(password)
        # user = 
        # user.is_admin = True
        # user.is_active = True
        # user.is_staff = True
        # user.is_superuser = True
        # user.save(using=self._db)
        return self.create_user(phone_number,password, **extra_fields)