from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

def home(request):
	return render(request, 'home.html')


class Posts(View):
    title = 'Posts'
    template = 'posts.html'

    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.values('pk', 'title', 'description'))

        context = {
            'title': self.title,
            'props': posts,
        }

        return render(request, self.template, context)
