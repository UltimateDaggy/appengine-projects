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

        #Specifying Login/Logout button
        account_action = users.get_current_user()

        if account_action == None:
            account_action_text = 'Login'
            account_action_url = users.create_login_url(self.request.uri)
        else:
            account_action_text = 'Logout'
            account_action_url = users.create_logout_url(self.request.uri)

        # get our template
        template = get_template({
            'comments' : comment_model.get_comments(),

            #google account stuff
            'display_user_account' : account_user,
            
            #login/Logout button
            'url_link_text' : account_action_text,
            'url_account_action' : account_action_url,
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
