#!/usr/bin/env python

import jinja2
import webapp2

from app.model import comment_model
from google.appengine.api import users

class AppController(webapp2.RequestHandler):
    def get(self):
        #Stop displaying None if no one signed in
        account_user = users.get_current_user()

        if account_user == None:
            account_user = ''

        # get our template
        template = get_template({
            'comments' : comment_model.get_comments(),
            #google account stuff
            'display_user_account' : account_user,
            
            #login button
            'url_link_text' : 'log-in',
            'url_account_action' : users.create_login_url(self.request.uri),
            #temporary logout button
            'logout_link_text' : 'log-out',
            'temp_logout' : users.create_logout_url(self.request.uri),
            })

        # return it to the browser
        self.response.out.write(template)

def get_template(data):
    # prepare our templating engine
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('app/view/'))

    # get our template
    template = env.get_template('app.html')

    # render our template
    return template.render(data)
