from django.shortcuts import render, get_object_or_404
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
