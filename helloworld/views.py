from django.shortcuts import render

def post_list(request):
    return render(request, 'helloworld/post_list.html', {})
