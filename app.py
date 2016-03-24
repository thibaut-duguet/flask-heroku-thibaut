"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
import module_mongolab as mlab
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hello_post():
    text = request.form['text']
    if mlab.alreadyInCollection(text):
        return redirect(url_for('results', query = text))
    else:
        mlab.uploadToMongolab(text)
        return render_template('index1.html')

@app.route('/results/<query>')
def results(query):
    community1 = mlab.communityInfo(query,0)
    community2 = mlab.communityInfo(query,1)
    community3 = mlab.communityInfo(query,2)
    community4 = mlab.communityInfo(query,3)
    return render_template('results.html', community1 = json.dumps(community1), community2 = json.dumps(community2),
        community3 = json.dumps(community3), community4 = json.dumps(community4), query = query)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('results.html')


###
# The functions below should be applicable to all Flask apps.
###

#@app.route('/<file_name>.txt')
#def send_text_file(file_name):
#    """Send your static text file."""
#    file_dot_text = file_name + '.txt'
#    return app.send_static_file(file_dot_text)


#@app.after_request
#def add_header(response):
#    """
#    Add headers to both force latest IE rendering engine or Chrome Frame,
#    and also to cache the rendered page for 10 minutes.
#    """
#    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#    response.headers['Cache-Control'] = 'public, max-age=600'
#    return response


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run(debug=True)
