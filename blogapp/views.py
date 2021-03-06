from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None


    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) # 3 posts in each page
    page = request.GET.get('page')
    try:
        plist = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        plist = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        plist = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()  

    return render(request,'blog/post/detail2.html',{'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form,'plist':plist})

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/index.html',{'page': page,'posts': posts})

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
            # ... send email

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,'form': form})

def contact(request):
    return render(request,'blog/post/contact.html')