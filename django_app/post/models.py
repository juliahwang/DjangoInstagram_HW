from django.db import models
# member앱에서 지정한 User모델을 사용하기 위해
# 프로젝트 폴더에서 settings를 불러온다.
from config import settings


# Create your models here.


class Post(models.Model):
    # member에서 정의한 User모델(Django가 제공하는 기본 User)을 받아옴.
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    # 사진을 올릴 때는 ImageField를 사용하고 pip을 이용해 Pillow라이브러리를 설치해준다.
    # 업로드 경로를 post로 지정한다.
    photo = models.ImageField(upload_to='post', blank=True)
    # 작성일은 작성시의 시간이 자동으로 등록되는 auto_now_add옵션을 사용
    created_date = models.DateTimeField(auto_now_add=True)
    # 수정시각에 따라 시간이 계속 업데이트되는 auto_now옵션을 사용
    modified_date = models.DateTimeField(auto_now=True)
    # User모델과 다대다필드를 생성하고 중간자 모델을 정의.
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike',
        # User모델을 받아오는 필드가 2개이므로 이름을 변경해준다.
        related_name='liked_post',
    )


# Post와 User모델 간의 중간자 모델 정의
class PostLike(models.Model):
    # Post 모델을 일대다로 받아오는 post 필드 생성
    post = models.ForeignKey(Post)
    # User 모델을 일대다로 받아오는 user 필드 생성
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # 댓글 작성일이라는 추가 필드를 생성하기 위해 중간자 모델 생성
    # 역시 auto_now_add=True를 사용한다.
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # User모델과 일대다로 연결되는 필드 생성
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    # Post모델과 일대다로 연결되는 필드 생성
    post = models.ForeignKey(Post)
    # 댓글내용을 작성할 수 있는 필드 생성. 제한이 없으므로 TextField 사용
    content = models.TextField()
    # 생성일은 auto_now_add=True
    created_date = models.DateTimeField(auto_now_add=True)
    # 수정일은 수정시마다 업데이트되므로 auto_now=True
    modified_date = models.DateTimeField(auto_now=True)
