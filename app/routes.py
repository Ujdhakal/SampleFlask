from flask import Blueprint, render_template, redirect, url_for
from app import db
from app.models import ContactSubmission
from app.forms import ContactForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        submission = ContactSubmission(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(submission)
        db.session.commit()
        return redirect(url_for('main.submissions'))
    return render_template('contact.html', form=form)

@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/submissions')
def submissions():
    contact_submissions = ContactSubmission.query.all()
    return render_template('submissions.html', contact_submissions=contact_submissions)


# Error handling
@main.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="404 - Page Not Found"), 404

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error="500 - Internal Server Error"), 500
