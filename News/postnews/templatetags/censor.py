from django import template

register = template.Library()


@register.filter()
def censor(value):

    words = ['редиска']

    text_one = value.split()
    main_text = ''

    for word in text_one:
        if word in words:
            censor = f'{word[:1]}' + (len(word)-1) * '*'
            if main_text == '':
                main_text += censor
            else:
                main_text += ' ' + censor
        elif main_text == '':
            main_text += word
        else:
            main_text += ' ' + word

    return f'{main_text}'
