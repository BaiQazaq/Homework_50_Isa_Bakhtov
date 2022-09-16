from django.shortcuts import render

from webapp.db import Cat


def action_view(request):
    if request.method == 'GET':
        return render(request, 'cat_create.html')
    print(f"ACTION=ACTION=ACTION GET GET", request.GET)
    print(f"ACTION=ACTION=ACTION POST POST", request.POST.get('action'), request.POST.get('name'))
    cat = Cat()
    if request.POST.get('action') is None and request.POST.get('name') is not None:
        cat.get_name(request.POST.get('name'))
        cat.get_age()
    else:
        cat.action_by_cat(request.POST.get('action'))
    img_cat = cat.var_image()
    print(str(img_cat), type(img_cat))
    context = {
        'name': Cat.name,
        'age': Cat.age,
        'feeling': Cat.feeling,
        'feeding': Cat.feeding,
        'state': Cat.sleep,
        'img_cat': img_cat
    }
    return render(request, 'action.html', context=context)
