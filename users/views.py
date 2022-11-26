from django.shortcuts import render
from .forms import UserForm, ResolveQuery
from django.http import HttpResponseRedirect
from .models import UserQuery, AgentResponse

# Create your views here.

def get_user_query(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = UserForm()
    return render(request, 'form.html', {'form': form})


def success_page(request):
    return render(request, 'success.html')


def resolve_query(request):
    id = request.get_full_path().strip().split('/')[-2]
    query = UserQuery.objects.get(pk=id)
    query.resolved = 'Assigned'
    query.save()
    other_queries = UserQuery.objects.filter(userID=query.userID).exclude(pk=id).exclude(resolved='Resolved').order_by('-timestamp')

    if request.method == 'POST':
        form = ResolveQuery(request.POST)
        if form.is_valid():
            query.resolved = 'Resolved'
            query.save()
            response = form.cleaned_data['response']
            list_of_other_queries = request.POST.getlist('other')
            all_queries = [id] + list_of_other_queries
            UserQuery.objects.filter(id__in=list_of_other_queries).update(resolved='Resolved')

            agent_response = AgentResponse(agent_name = request.user.username,
            userID = query.userID,
            queries_handled = all_queries,
            query_response = response
            )

            agent_response.save()

            return HttpResponseRedirect('/admin/users/userquery')
    else:
        form = ResolveQuery()
    
    return render(request, 'admin/resolve_query.html', {'query': query, 'form': form, 'other_queries': other_queries})


def unresolve_query(request):
    id = request.get_full_path().strip().split('/')[-2]
    query = UserQuery.objects.filter(pk=id).update(resolved='Open')
    return HttpResponseRedirect('/admin/users/userquery')


def transfer_query(request):
    id = request.get_full_path().strip().split('/')[-2]
    query = UserQuery.objects.filter(pk=id).update(resolved='Open')
    return HttpResponseRedirect('/admin/users/userquery')