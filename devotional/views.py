from devotional.models import Devotional
from django.shortcuts import render_to_response
from django.template import RequestContext


def get_devotional(request, month, day):
    devotionals = Devotional.objects.filter(month = month, day = day)
    return render_to_response('devotional_list.html', {
        'devotionals': devotionals
    }, context_instance=RequestContext(request))


def get_devotional_with_count(request, month, day):
    devotionals = Devotional.objects.filter(month = month, day = day)
    total_count = 0
    for dev in devotionals:
        total_count += len(dev.body.split())

    return render_to_response('devotional_list_with_count.html', {
        'devotionals': devotionals,
        'count': total_count
    }, context_instance=RequestContext(request))



def get_devotionals_count(request):

    devotionals = Devotional.objects.all()
    total_count = 0
    for dev in devotionals:
        total_count += len(dev.body.split())

    return render_to_response('devotional_count.html', {
        'count': total_count
    }, context_instance=RequestContext(request))
