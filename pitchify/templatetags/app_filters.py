from django import template
from pitchify.models import Offer

register = template.Library()


@register.filter(name='get_offer_status')
def get_offer_status(key, status):
    for v in Offer.STATUS_CHOICES:
        if (v[0] == status):
            return v[1]