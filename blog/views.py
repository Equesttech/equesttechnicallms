from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPost

class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'post_list'
    template_name = 'blog/blog_index.html'
    paginate_by = 3

# Keeping this for now
# class post_detail(generic.DetailView):
#     model = BlogPost
#     template_name = 'blog/video_post_detail.html'


# Comment posting

def post_detail(request, slug):
    template_name = 'blog/blog_post_detail.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
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

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
