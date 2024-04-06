from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="profile_pics/", default="user.png")
    # city = models.CharField(max_length=255, blank=True, null=True)
    # shop_name = models.CharField(max_length=255, blank=True, null=True, default="None")
    # add another fields here if required



    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = MyAccountManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

# from django.db import models
# from django.contrib.auth.models import User
# from base.models import BaseModel
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import uuid
# from base.emails import send_account_activation_email

# class Profile(BaseModel):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
#     is_email_verified = models.BooleanField(default=False)
#     email_token = models.CharField(max_length=100, null=True, blank=True)
#     profile_image = models.ImageField(upload_to='profile')
    

# import logging

# @receiver(post_save, sender=User)
# def send_email_token(sender, instance, created, **kwargs):
#     try:
#         if created:
#             email_token = str(uuid.uuid4())
#             Profile.objects.create(user=instance, email_token=email_token)
#             email = instance.email
#             send_account_activation_email(email, email_token)

#     except Exception as e:
#         logging.error(f"Error sending activation email: {e}")
