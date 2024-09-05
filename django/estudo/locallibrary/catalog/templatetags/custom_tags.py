from django import template

register = template.Library()


def get_range(value):
    return range(1, value + 1)

@register.simple_tag
def rate_next_pages (page, current_page, num_pages):

    if page == current_page:
        return True
    elif current_page == page -1 and page != 3:
        return True
    elif current_page == page +1:
        return True
    elif page <= num_pages and page > num_pages -2:
        return True
    else:
        return False

@register.simple_tag
def rate_last_pages (num_pages, current_page,  page_for):
    if current_page != num_pages -1 and current_page != num_pages -2:
        if page_for <= num_pages and page_for > num_pages -2:
            return True
        else:
            return False
    else:
        return False

@register.simple_tag
def rate_first_last_pages (num_pages,  page_for, current_page):
    if page_for == num_pages -2 and current_page > 2 and (current_page != num_pages):
        print(num_pages, page_for)
        return True
    else:
        return False
    

def next_pages(value, value2):
    if value == 3:
        return True
    else:
        return True

def previus_pages(value):
    return value - 1


register.filter('get_range', get_range)
register.filter('next_pages', next_pages)
register.filter('previus_pages', previus_pages)

