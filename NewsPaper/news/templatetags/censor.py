from django import template

register = template.Library()

CENSOR_WORDS = ['редиска', 'спартак']

test_text = 'Спартак просрал, игрок-редиска забил сам себе'


@register.filter()
def censor(text):
    if not isinstance(text, str):
        raise TypeError('Фильтр применяется только для строк')

    for cens in CENSOR_WORDS:
        if cens.find(text.lower()):
            text = text.replace(cens[1:], '*' * (len(cens) - 1))

    return f'{text}'



