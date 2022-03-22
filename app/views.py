"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
import os
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for,flash,send_from_directory


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/properties/create', methods=["GET", "POST"])
def create():
    form = PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            Title = form.title.data
            Bedrooms = form.bedrooms.data
            Bathrooms = form.bathrooms.data
            Location = form.location.data
            Price = form.price.data
            Proptype = form.proptype.data 
            Description = form.description.data
            filename = secure_filename(form.img.data.filename)
            form.img.data.save(app.config['UPLOAD_FOLDER']+'/'+filename)
            prop = Property(Title,Bedrooms,Bathrooms,Location,Price,Proptype,Description,filename)
            db.session.add(prop)
            db.session.commit()
            flash('Property Registered', 'success')
            return redirect(url_for('properties'))

    return render_template('create.html',form=form)

@app.route('/properties')
def properties():
    print(Property.query.all()[0].img)
    return render_template('properties.html',propert = Property.query.all(),get_image= get_image)

    
@app.route('/img/<filename>')   
def get_image(filename):
    di = os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=di, path=filename)

@app.route('/properties/<propertyid>')
def propertyview(propertyid):
    return render_template('propertyview.html',pr= Property.query.get(propertyid),get_image= get_image)    

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
