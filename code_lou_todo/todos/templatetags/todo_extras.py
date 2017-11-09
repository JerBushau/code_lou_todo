from django import template

register = template.Library()


# custom filter to concat strings, built-in |add: filter was not working
# for my purposes (trying to concat an int to a str)
@register.filter
def addstr(arg1, arg2):
    """ concatenate arg1 & arg2 """

    return str(arg1) + str(arg2)

