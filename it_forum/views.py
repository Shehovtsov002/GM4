from it_forum.forms import ItForumForm
from django.shortcuts import get_object_or_404
from it_forum.models import ItForum
from django.views import generic


class AnswersListView(generic.ListView):
    template_name = 'crud/answer_list.html'
    context_object_name = 'answer'
    model = ItForum

    def get_queryset(self):
        return self.model.objects.all()


class AnswerDetailView(generic.DetailView):
    template_name = 'crud/answer_detail.html'
    context_object_name = 'answer_id'
    model = ItForum

    def get_object(self, **kwargs):
        answer_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=answer_id)


class AnswerCreateView(generic.CreateView):
    template_name = 'crud/create_answer.html'
    form_class = ItForumForm
    success_url = '/answer_list/'

    def form_valid(self, form):
        return super(AnswerCreateView, self).form_valid(form=form)


class AnswerDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/answer_list/'
    model = ItForum

    def get_object(self, **kwargs):
        answer_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=answer_id)


class AnswerUpdateView(generic.UpdateView):
    template_name = 'crud/edit_answer.html'
    form_class = ItForumForm
    success_url = '/answer_list'
    model = ItForum

    def form_valid(self, form):
        return super(AnswerUpdateView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        answer_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=answer_id)


# def create_answer_it_forum_view(request):
#     if request.method == 'POST':
#         form = ItForumForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Answer create successfully</h1>')
#     else:
#         form = ItForumForm()
#     return render(request, template_name='crud/create_answer.html', context={'form': form})


# def answer_list_it_forum_view(request):
#     if request.method == 'GET':
#         answer = ItForum.objects.all()
#         return render(request, template_name='crud/answer_list.html', context={'answer': answer})


# def answer_detail_it_forum_view(request, answer_id):
#     if request.method == 'GET':
#         answer = get_object_or_404(ItForum, id=answer_id)
#         return render(request, template_name='crud/answer_detail.html', context={'answer_id': answer})


# def delete_answer_it_forum_view(request, answer_id):
#     answer = get_object_or_404(ItForum, id=answer_id)
#     answer.delete()
#     return HttpResponse('Answer deleted successfully!')


# def update_answer_it_forum_view(request, answer_id):
#     answer = get_object_or_404(ItForum, id=answer_id)
#     if request.method == 'POST':
#         form = ItForumForm(request.POST, instance=answer)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Answer updated successfully</h1>')
#     else:
#         form = ItForumForm(instance=answer)
#     return render(request, template_name='crud/edit_answer.html', context={'form': form})

class SearchAnswerView(generic.ListView):
    template_name = 'crud/answer_list.html'
    context_object_name = 'answer'
    paginate_by = '5'

    def get_queryset(self):
        return ItForum.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
