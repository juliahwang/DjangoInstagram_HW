from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# 아래의 모델을 AUTH_USER_MODEL로 사용하도록
# settings에 설정해준다.
class User(AbstractUser):
    pass
