from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    story = Story.objects.first()
    context = {
        'story' : story,
        'questions' : story.question_set.all() 
    }
    
    return render(request, 'index.html', context)

def test(request, id):
    story = Story.objects.first()
    question = story.question_set.get(pk=int(id))
    
    if request.method == 'POST':
        if question:
            selected = request.POST.get(str(question.question))
        try:
            chosen_option = story.question_set.get(pk=selected)
            print(chosen_option)
        except (KeyError, Question.DoesNotExist):
            return render(request, 'test.html', context)

        else:
            if chosen_option == question.answer:
                story.score += 1
                story.save()

        return HttpResponseRedirect(reverse('result', kwargs={'pk' : question.id}))
   
    else:
        context = {
            'story' : story,
            'questions' : story.question_set.all(),
            'question' :  question
        }

        return render(request, 'test.html', context)


def result(request):
    story = Story.objects.first()
    context = {
        'story' : story
    }

    return render(request, 'result.html', context)