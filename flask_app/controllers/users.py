from flask import render_template, redirect, request, flash
from flask_mail import Message
from flask_app.models.user import PreUser
from flask_app.models.product import Product
from flask_app import app
from flask_app import mail  


@app.route('/register', methods=['POST'])
def register():
    try:
        # Your registration logic...
        
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        city = request.form['city']
        state = request.form['state']
        message = request.form['message']
        
        # Send email notification with all form data included
        msg = Message("New User Registration", 
                      sender="camerona321@gmail.com",  
                      recipients=['devCameronAngeleri@gmail.com'])  
        
        msg.body = f"""A new user has registered on your website! 
                      Details:
                      First Name: {first_name}
                      Last Name: {last_name}
                      Email: {email}
                      City: {city}
                      State: {state}
                      Message: {message}
                   """
        mail.send(msg)
        
        flash('Registration successful! An email notification has been sent to the admin.', 'success')
    except Exception as e:
        flash('An error occurred while sending the email notification. Please try again later.', 'error')
        app.logger.error(f"Error sending email notification: {str(e)}")
    
    return redirect(url_for('index'))

@app.route('/registration')
def reg_page_display():
    products = Product.get_all()
    return render_template("reg_page.html", products=products)

@app.route('/pre_register', methods=['POST'])
def pre_register():
    form_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'city': request.form['city'],
        'state': request.form['state'],
        'message': request.form['message']
    }
    
    if not PreUser.validate_pre_user(form_data):
        return redirect('/registration')
    
    # Save pre-user data
    PreUser.save(form_data)

    flash(f'Thank you {form_data["first_name"]}! I cannot wait to connect with you!', 'registration')
    return redirect('/')
