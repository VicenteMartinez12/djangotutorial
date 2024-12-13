from django.shortcuts import render

# Create your views here.
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.test import TestCase

# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     context = {"latest_question_list": latest_question_list}
# #     return render(request, "polls/index.html", context)


# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     template = loader.get_template("polls/index.html")
# #     context = {
# #         "latest_question_list": latest_question_list,
# #     }
# #     return HttpResponse(template.render(context, request))

# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     output = ", ".join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)


# # def index(request):
# #     return HttpResponse("Hola mundo, este es la pagina de inicio para el proyecto de django")

# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)

# # ...
# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, "polls/detail.html", {"question": question})

# # ...
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


# # def vote(request, question_id):
# #     return HttpResponse("You're voting on question %s." % question_id)


from django.http import HttpResponse
from django.views.generic import View


def service_worker(request):
    return HttpResponse(open('static/service-worker.js').read(), content_type='application/javascript')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
# class DetailView(generic.DetailView):

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
    
    
# def get_queryset(self):
#     """
#     Return the last five published questions (not including those set to be
#     published in the future).
#     """
#     return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
#         :5
#     ]
    
# class QuestionDetailViewTests(TestCase):
#     def test_future_question(self):
#         future_question = create_question(question_text="Future question.", days=5)
#         url = reverse("polls:detail", args=(future_question.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)

#     def test_past_question(self):
#         past_question = create_question(question_text="Past Question.", days=-5)
#         url = reverse("polls:detail", args=(past_question.id,))
#         response = self.client.get(url)
#         self.assertContains(response, past_question.question_text)