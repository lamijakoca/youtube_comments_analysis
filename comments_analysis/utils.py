import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_id(url):
    return url.split('?v=')[-1]

def get_video_comments(url):
    video_id = get_video_id(url)
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    )
    
    while request:
        response = request.execute()
        for item in response['items']:
            comment_info = {
                'text': item['snippet']['topLevelComment']['snippet']['textDisplay'],
                'likeCount': item['snippet']['topLevelComment']['snippet'].get('likeCount')
            }
            comments.append(comment_info)
        request = youtube.commentThreads().list_next(request, response)

    return comments

def filter_questions(comments):
    questions = []

    for comment in comments:
        text_display = comment['text']
        like_count = comment['likeCount']
        if '?' in text_display and like_count >= 1:
            questions.append({
                'question': text_display,
                'likeCount': like_count
            })
    return questions

def get_top_liked_questions(comments, top=10):
    sorted_questions = sorted(comments, key=lambda x: x['likeCount'], reverse=True)
    return sorted_questions[:top]
