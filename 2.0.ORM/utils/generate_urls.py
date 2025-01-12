from django.urls import path


def generate_urls(view_class, name, actions):
    return [
        path(f'{action}/', view_class.as_view(),
             {'action': action, 'name': name}, name=f'{name}_{action}')
        for action in actions
    ]
