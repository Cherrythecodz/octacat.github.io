# settings.py
INSTALLED_APPS = [
    # ...
    'channels',
    # ...
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  # Use Redis or other backends in production
    },
}

ASGI_APPLICATION = '<your_project_name>.asgi.application'
