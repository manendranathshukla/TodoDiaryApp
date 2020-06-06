from django.shortcuts import render,redirect

# Create your views here.
from .models import TodoModel


def index(request):
    mytodo = TodoModel.objects.all()
    #print(mytodo)
    st={
        "mytask":mytodo
    }

    return render(request,"index.html",st)



def addtask(request):
    mytask=request.POST['task']
    TodoModel(task=mytask).save()
    return redirect(request.META['HTTP_REFERER'])
    

def removetask(request,taskpk):
    TodoModel.objects.filter(id=taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])


def updatetaskview(request,taskpk):
    context={"todopk":taskpk}
    return render(request,"updatetask.html",context)


def updatetask(request,taskpk):
    usertask=request.POST['task']
    todo_update=TodoModel.objects.filter(id=taskpk)[0]
    todo_update.task=usertask
    todo_update.save()
    return redirect("homepage")