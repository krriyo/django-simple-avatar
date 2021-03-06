from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib import messages

from forms import AvatarForm

from djangohelper.helper import request_get_next

def change(request, template_name='avatar/change.html', extra_context={}, next=None):
    avatar_form = AvatarForm(user=request.user)
    if request.method == "POST":
        avatar_form = AvatarForm(request.POST, request.FILES, user=request.user)
        if  avatar_form.is_valid():
            avatar_form.save()
            updated_message=_("Successfully updated your avatar.")
            messages.add_message(request, messages.INFO, updated_message)
        return HttpResponseRedirect(request_get_next(request) or next)
    return render_to_response(
        template_name,
        extra_context,
        context_instance = RequestContext(
            request,
            { 'avatar_form': avatar_form,
              'next': request_get_next(request) or next, }
        )
    )
change = login_required(change)
