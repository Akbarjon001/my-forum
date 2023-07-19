from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models


# Create your views here.


def MainView(request):
    return render(request, 'main/mainPage.html')


@login_required(login_url='/users/register')
def ForumView(request):
    topics = models.Topics.objects.all()
    print(topics)
    return render(request, 'forum/topics.html', context={'topics': topics})


@login_required(login_url='/users/register')
def CreateTopicView(request):
    if request.method == 'POST':
        user = request.user
        data = request.POST.dict()
        image = request.FILES.get('photo', None)
        topic = models.Topics(title=data['title'], body=data['description'], user=user, image=image,
                              category=data['select'])
        topic.save()
    return render(request, 'forum/create_topic.html')


@login_required(login_url='/users/register')
def TopicView(request, topic_id):
    if request.method == 'POST':
        user = request.user
        data = request.POST.dict()
        topic = models.Topics.objects.get(id=data['topic_id'])
        new_comment = models.Comments(author=user, text=data['comment'], in_topic=topic)
        new_comment.save()
        return redirect(f'/topics/{data["topic_id"]}')
    else:
        topic = models.Topics.objects.get(id=topic_id)
        comments = models.Comments.objects.filter(in_topic=topic_id)
        return render(request, 'forum/show_topic.html', context={'topic': topic, 'comments': comments})
    

@login_required(login_url='/users/register')
def CategoriesView(request):
    back_end = models.Topics.objects.filter(category='back-end').count()
    front_end = models.Topics.objects.filter(category='front-end').count()
    others = models.Topics.objects.filter(category='others').count()
    full_stack = models.Topics.objects.filter(category='full-stack').count()
    js = models.Topics.objects.filter(category='java-script').count()
    python = models.Topics.objects.filter(category='python').count()
    return render(request, 'categories/show_categories.html',
                  context={
                      'back_end': back_end,
                      'front_end': front_end,
                      'others': others,
                      'full_stack': full_stack,
                      'js': js,
                      'python': python
                  })


@login_required(login_url='/users/register')
def CategoryView(request, type_category):
    topics = models.Topics.objects.filter(category=type_category)
    return render(request, 'categories/show_category.html', context={'topics': topics})


@login_required(login_url='/users/register')
def ContactView(request):
    return render(request, 'contact/contact.html')