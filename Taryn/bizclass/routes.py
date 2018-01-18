# This is te workhorse code for this app. We import some tools and then
# set up some functions to handle specific URL's. These functions are also
# know as "view functions"


from flask import render_template, flash, redirect, url_for
from bizclass import app
from bizclass.forms import LoginForm, BizClassForm

# If the web URL matches either of these two then we'll set up
# some variables and pass them as args to the index.html URL to
# be processed and rendered back to users browser.
#
# Note that although we could have written the HTML in these view functions it
# is easier to manage if we state that externally in its own index.html file
# otherwise referred to as a template (and processed by render_template)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kenneth',
            'group':'EA'}
    posts = [
        {
            'author': {'username': 'Srini'},
            'body': 'New release of ScaleIO'
        },
        {
            'author': {'username': 'Dave'},
            'body': 'vSAN 6.3 has bugs'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

# Here's another view function with some extra logic.
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# Here's another view function with some extra logic.
@app.route('/bizclass', methods=['GET','POST'])
def bizclass():
    biz_class_form = BizClassForm()
    if biz_class_form.validate_on_submit():
        flash('Business Class modelling for user {}, remember_me={}'.format(biz_class_form.application.data, biz_class_form.remember_me.data))
        return redirect(url_for('bizclass'))
    return render_template('bizclass.html', title='Business Class', form=biz_class_form)
