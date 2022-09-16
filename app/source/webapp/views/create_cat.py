from django.shortcuts import render


def create_view(request):

    if request.method == 'GET':
        return render(request, 'cat_create.html')
    context = {
        'name': request.POST.get('name')
    }
    return render(request, 'action.html', context=context)
