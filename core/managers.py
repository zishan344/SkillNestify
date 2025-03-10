from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
  """Custom user manager to handle users with email as login credential."""
  def create_user(self, email, username, password=None, **extra_fields):
    """Create and return a user with an email, username, and password."""
    if not email:
      raise ValueError('email is required')
    if not username:
      raise ValueError('username is required')
    email = self.normalize_email(email)
    user = self.model(email=email,username=username, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self, email, username, password=None, **extra_fields):
    """ Create and return a superuser with the given email, username, and password. """
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, username, password, **extra_fields)

