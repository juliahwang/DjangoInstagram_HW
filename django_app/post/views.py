from django.shortcuts import render, get_object_or_404, redirect

from member.models import User
from .models import Post

# Create your views here.


def post_list(request):
    # posts에 쿼리셋으로 Post의 데이터를 모두 가져온다.
    posts = Post.objects.all()
    # context 딕셔너리에 render할 데이터를 넘겨준다.
    context = {
        'posts': posts,
    }
    # 요청이 들어오면 post/post_list.html에 context의 데이터를 렌더링해주는 함수.
    return render(request, 'post/post_list.html', context=context)


def post_detail(request, post_pk):
    # get_object_or_404(<모델명>, 추가인자):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post,
    }
    # 요청이 들어오면 post/post_detail.html에 context의 데이터를 렌더링해주는 함수.
    return render(request, 'post/post_detail.html', context=context)


def post_create(request):
    # request.method가 'GET'방식일 때
    if request.method == 'GET':
        context = {
        }
        # 단순히 post_create 템플릿을 렌더링해 보여준다.
        return render(request, 'post/post_create.html', context)
    # request.method가 'POST'방식일 때
    else:
        # post 생성
        post = Post.objects.create(
            author=User.objects.first(),
            # photo는 request의 FILES 딕셔너리에서 인풋 태그의 이름이
            # 'file'인 것을 찾아 할당해준다.
            photo=request.FILES['file'],
        )
        # reverse()함수를 사용하여 url을 만들고 해당 페이지로 렌더링할 경우
        # redirect(<이동할 url이름>, <추가인자>)함수를 사용한다
        return redirect('post:post_detail', post_pk=post.pk)
