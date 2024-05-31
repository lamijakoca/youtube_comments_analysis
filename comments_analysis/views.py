from django.shortcuts import render
from .forms import YouTubeForm
from .utils import get_video_comments, filter_questions, get_top_liked_questions

def index(req):
    if req.method == 'POST':
        form = YouTubeForm(req.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            comments = get_video_comments(url)
            questions = filter_questions(comments)
            top_questions = get_top_liked_questions(questions, top=10)
            return render(req, 'comments_analysis/results.html',{'questions':top_questions})
    else:
        form = YouTubeForm()
    return render(req, 'comments_analysis/index.html', {'form':form})
