from django.http import HttpResponse
from it_forum.forms import ItForumForm
from django.shortcuts import render, get_object_or_404

from it_forum.models import ItForum


def create_answer_it_forum_view(request):
    if request.method == 'POST':
        form = ItForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Answer create successfully</h1>')
    else:
        form = ItForumForm()
    return render(request, template_name='crud/create_answer.html', context={'form': form})


def answer_list_it_forum_view(request):
    if request.method == 'GET':
        answer = ItForum.objects.all()
        return render(request, template_name='crud/answer_list.html', context={'answer': answer})


def answer_detail_it_forum_view(request, answer_id):
    if request.method == 'GET':
        answer = get_object_or_404(ItForum, id=answer_id)
        return render(request, template_name='crud/answer_detail.html', context={'answer_id': answer})


def delete_answer_it_forum_view(request, answer_id):
    answer = get_object_or_404(ItForum, id=answer_id)
    answer.delete()
    return HttpResponse('Answer deleted successfully!')


def update_answer_it_forum_view(request, answer_id):
    answer = get_object_or_404(ItForum, id=answer_id)
    if request.method == 'POST':
        form = ItForumForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Answer updated successfully</h1>')
    else:
        form = ItForumForm(instance=answer)
    return render(request, template_name='crud/edit_answer.html', context={'form': form})
