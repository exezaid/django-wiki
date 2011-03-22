from wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def view_page(request, page_name):
  try:
    page = Page.objects.get(pk=page_name)
  except Page.DoesNotExist:
    return render_to_response('create.html', {'page_name': page_name})

  content = page.content
  return render_to_response("view.html", {"page_name":page_name, "content":content})


@csrf_protect
def edit_page(request, page_name):
  try:
    page = Page.objects.get(pk=page_name)
    content = page.content
  except Page.DoesNotExist:
    content= ""
  d = RequestContext(request,{'page_name':page_name, 'content':content})
  return render_to_response('edit.html',d )

@csrf_protect
def save_page(request, page_name):
  content = request.POST['content']
  try:
    page = Page.objects.get(pk=page_name)
    page.content = content
  except Page.DoesNotExist:
    page = Page(name=page_name, content=content)
  page.save()
  page = RequestContext(request, {'page': page})
  return HttpResponseRedirect("/wiki/" + page_name + "/")
