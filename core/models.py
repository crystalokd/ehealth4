from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class Appointment(models.Model):
    your_name = models.CharField(max_length=50)
    your_phone = models.CharField(max_length=50)
    your_email = models.CharField(max_length=50)
    your_schedule = models.CharField(max_length=50)
    your_message = models.CharField(max_length=50)
    doc_email = models.EmailField(default='none@email.com')
    approved = models.BooleanField('Aprroved', default=False)

    def __str__(self):
        return f'{self.your_name} Appointment'



# Create your CustomUserManager models here.
class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
		if not email:
			raise ValueError("Email must be provided")
		if not password:
			raise ValueError("Password is not provided")

		user = self.model(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			mobile = mobile,
			**extra_fields
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def _create_superuser(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email must be provided")
		if not password:
			raise ValueError("Password is not provided")

		user = self.model(
			email = self.normalize_email(email),
			
			**extra_fields
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_superuser(email, password, **extra_fields)



# Create your User models here.
class User(AbstractBaseUser, PermissionsMixin):
	# Abstractbaseuser has password, last_login, is_active by default

	email = models.EmailField(db_index=True, unique=True, max_length=254)
	first_name = models.CharField(max_length=248)
	last_name = models.CharField(max_length=255)
	mobile = models.CharField(max_length=50)

	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_physician = models.BooleanField(default=False)
	


	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	# REQUIRED_FIELD = ['first_name', 'last_name', 'mobile']

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'



class Profile(models.Model):
	choices = (("Yes", 'Yes'), ("No", 'No'))
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	Email = models.EmailField(default='none@email.com')
	first_name = models.CharField(max_length=248, default='none@email.com')
	Stomach_ach = models.CharField(max_length=255, choices=choices)
	Diarrheal = models.CharField(max_length=255, choices=choices)
	Injuries = models.CharField(max_length=255, choices=choices)
	Head_ache = models.CharField(max_length=255, choices=choices)
	Cough = models.CharField(max_length=255, choices=choices)

	def __str__(self):
	    return f'{self.Email} Profile'