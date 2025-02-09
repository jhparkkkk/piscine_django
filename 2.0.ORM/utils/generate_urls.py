from django.urls import path


def generate_urls(view_class, name, actions):
    # urls = [
    #    path('', view_class.as_view(), {
    #         'action': actions, 'name': name}, name=f'{name}_{actions}')
    # ]

    urls = [
        path(f'{action}/', view_class.as_view(),
             {'action': action, 'name': name}, name=f'{name}_{action}')
        for action in actions
    ]
    print(urls)
    return urls
