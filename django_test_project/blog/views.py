from django.shortcuts import render
from .models import Post

'''
posts = [
	{
		'author' : 'Dhiraj Singh',
		'title' : 'Blog post 1',
		'content' : 'First Post Content',
		'date_posted' : 'August 03, 2020'
	},
	{
		'author' : 'Neha Singh',
		'title' : 'Blog post 2',
		'content' : 'Second Post Content',
		'date_posted' : 'August 04, 2020'
	}
]
'''
def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html', {'title':'About'})	
