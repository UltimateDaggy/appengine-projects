#!/usr/bin/env python

import jinja2
import webapp2

from app.model import comment_model

class AppController(webapp2.RequestHandler):
    def get(self):
        # get our template
        template = get_template({
            'comments' : comment_model.get_comments()
        })

        # return it to the browser
        self.response.out.write(template)

#class MainPage(webapp2.RequestHandler):
    def get(self):
#        guestbook_name=self.request.get('guestbook_name')
#        greetings_query = Greeting.all().ancestor(
#            guestbook_key(guestbook_name)).order('-date')
#        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

#        template_values = {
#            'greetings': greetings,
#            'url': url,
#            'url_linktext': url_linktext,
#        }

#        template = jinja_environment.get_template('index.html')
            #the templates being 'get' below... is that where i need to add this code? 
#        self.response.out.write(template.render(template_values))
            #if i'm not using template_values then this isn't needed, right?        

def get_template(data):
    # prepare our templating engine
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('app/view/'))

    # get our template
    template = env.get_template('app.html')

    # render our template
    return template.render(data)
