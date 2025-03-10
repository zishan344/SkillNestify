from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from core.managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
  """ Custom user model """
  SELLER ='seller'
  BUYER = 'buyer'
  USER_TYPE_CHOICE = [
    (SELLER, 'seller'),
    (BUYER, 'buyer'),
  ]
  username = models.CharField(max_length=20, unique=True)
  email = models.EmailField(unique=True)
  user_type = models.CharField(max_length=10,
                              choices=USER_TYPE_CHOICE, default=BUYER)
  address = models.TextField(blank=True, null=True)
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  objects = CustomUserManager()
  
  def __str__(self):
      return self.email

  def save(self, *args, **kwargs):
    # Save the user first
    super().save(*args, **kwargs)
    
    # Get the group name
    group_name = self.user_type
    group, created = Group.objects.get_or_create(name=group_name)
    
    for user_type, _ in self.USER_TYPE_CHOICE:
      if user_type != self.user_type:
        other_group = Group.objects.filter(name=user_type).first()
        if other_group and self in other_group.user_set.all():
          other_group.user_set.remove(self)
    group.user_set.add(self)

