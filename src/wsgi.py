# starts app as WSGI | used e.g. in start_server script for staging/production
# can't include the create_wsgi_app (imported in package dunder init) here,
# otherwise app will be created every time => this should be separate file 🔥

from create_wsgi_app import create_wsgi_app

app = create_wsgi_app()  # shouldn't be behind "if __name..."
