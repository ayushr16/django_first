from django import template

register = template.Library()

def cut(value,args):

    return value.replace(arg,'')

register.filter('cut',cut)
