from django.shortcuts import render
from django.shortcuts import render_to_response
from posts.models import *
from django.template import RequestContext
from forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime
from django.contrib.auth.models import User

# Create your views here.

def posts(request):
	if request.user.is_authenticated():
		form = CommentForm()
		args = {}
		args.update(csrf(request))
		args['comment'] = Comment.objects.all()
		args['form'] = form
		args['posts'] = Post.objects.all()
		args['uuid'] = request.user.id
		following = Follow.objects.filter(fuser=request.user)
		fposts = Post.objects.filter(user__following__fuser=request.user)
		args['fposts'] = fposts
		return render_to_response('loggedin.html', args )
	else:
		args = {}
		args.update(csrf(request))
		args.update(csrf(request)) 
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)

def post(request,post_id=1):
	if request.user.is_authenticated():
		args = {}
		args['comment'] = Comment.objects.filter(post=Post.objects.filter(id=post_id))
		args['post'] = Post.objects.get(id=post_id)
		form = CommentForm()
		args['form'] = form
		args['uuid'] = request.user.id
		return render_to_response('post.html',args,RequestContext(request))
	else:
		args = {}
		args.update(csrf(request)) 
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)

def myposts(request):
	if request.user.is_authenticated():
		args = {}
		args.update(csrf(request))
		args['comment'] = Comment.objects.filter(post=Post.objects.filter(user=request.user))
		args['posts'] = Post.objects.filter(user=request.user)
		form = CommentForm()
		args['form'] = form
		args['uuid'] = request.user.id
		
		stalks = Stalk.objects.filter(stalked=request.user)
		print stalks
		L=[]
		for stalk in stalks:
			if (stalk.ctr>=10):
				print stalk.ctr
				L.append(stalk.stalker.username)
				stalk.ctr=0
				stalk.save()


		args['stalks']= L
		return render_to_response('myposts.html',
					  args,
				   	  RequestContext(request))
	else:
		args = {}
		args.update(csrf(request))
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)

def create(request):
	if request.POST:		
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			f2 = form.save(commit=False)
			f2.pub_date = datetime.datetime.now()
			f2.user = request.user
		        f2.save()
			return myposts(request)
	else:
		form = PostForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('create.html',args)


def like_post(request,post_id=1):
	if request.user.is_authenticated():
		if post_id:
			num = Like.objects.filter(user=request.user,post=Post.objects.filter(id=post_id)).count()
			if (num == 0):
				a = Post.objects.get(id=post_id)
				a.likes += 1
				a.save()
			
				l = Like(post=a,user=request.user)
				l.save()
		return posts(request)
	else:
		args = {}
		args.update(csrf(request))
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)


def delete_post(request,post_id=1):
	if request.user.is_authenticated():
		if post_id:
			Post.objects.filter(id=post_id).delete()
		return myposts(request)
	else:
		args = {}
		args.update(csrf(request)) 
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)

def create_comment(request,post_id=1):
	if request.user.is_authenticated():
		if request.POST:		
			form = CommentForm(request.POST)
			if form.is_valid():
				f2 = form.save(commit=False)
				f2.pub_date = datetime.datetime.now()
				f2.user = request.user
				f2.post = Post.objects.get(id=post_id)
				f2.pid = post_id
				f2.uid = request.user.id
				f2.save()
				return HttpResponseRedirect('/')
	else:
		args = {}
		args.update(csrf(request)) 
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)


def delete_comment(request,comment_id=1):
	if request.user.is_authenticated():
		if comment_id:	
			Comment.objects.filter(id=comment_id).delete()
		return posts(request)
	else:
		args = {}
		args.update(csrf(request)) 
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)

def show_user(request,user_id=1):
	if request.user.is_authenticated():
		if int(request.user.id)==int(user_id):
			return myposts(request)
		else:
			try:
				a = Stalk.objects.get(stalked=User.objects.get(id=user_id),stalker=request.user)
				a.ctr+=1
				a.save()
			except:
				a = Stalk(stalked=User.objects.get(id=user_id),stalker=request.user)
				a.save()
			args = {}
			args.update(csrf(request))
			args['comment'] = Comment.objects.all()
			args['posts'] = Post.objects.filter(user=User.objects.filter(id=user_id))
			args['showuser'] = User.objects.get(id=user_id)
			form = CommentForm()
			args['form'] = form
			args['uuid'] = request.user.id
			return render_to_response('show.html',
						  args,
					   	  RequestContext(request))
	else:
		args = {}
		args.update(csrf(request))
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)


def like_comment(request,comment_id=1):
	if request.user.is_authenticated():
		if comment_id:
			num = CLike.objects.filter(user=request.user,comment=Comment.objects.filter(id=comment_id)).count()
			if (num == 0):
				a = Comment.objects.get(id=comment_id)
				a.likes += 1	
				a.save()

				l = CLike(comment=a,user=request.user)
				l.save()
		return posts(request)
	else:
		args = {}
		args.update(csrf(request))
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)


def follow_user(request,user_id=1):
	if request.user.is_authenticated():
		if user_id:
			num = Follow.objects.filter(fuser=request.user,fduser=User.objects.filter(id=user_id)).count()
			if (num == 0):
				a = Follow(fuser=request.user,fduser=User.objects.get(id=user_id))
				a.save()
		return posts(request)
	else:
		args = {}
		args.update(csrf(request))
		args['error'] = '**PLEASE SIGN IN FIRST**'
		return render_to_response('index.html', args)







	
	

