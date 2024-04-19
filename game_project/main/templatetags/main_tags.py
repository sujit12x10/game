from django import template
from main.models import Team, Season
from django.db.models import Count
from collections import OrderedDict
import json

register = template.Library()

@register.filter
def points(obj):
    for key, values in obj.items():
        if key == 'wins':
            return obj[key] * 2
        
@register.filter   
def order(obj):
    new_dict = OrderedDict(sorted(obj.items(), key=lambda kv:kv[1]['wins'], reverse=True))
    return new_dict

@register.filter
def playoffs(obj):
    simple_dict = json.loads(json.dumps(obj))
    return simple_dict
