from django import template
  
register = template.Library()
  
@register.filter()
def ownerize(value):
    OWNER_NAMES = {
        'father': 'پدر',
        'mother': 'مادر',
        'son': 'پسر',
        'daughter': 'دختر',
    }
    return OWNER_NAMES[value]