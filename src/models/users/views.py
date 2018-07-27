from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
import src.models.users.errors as UserErrors
from src.models.users.users import User

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
# Two options when user arrives at login page: She wants to see login page: GET request or she is submitting data which we are putting into database: POST request
def login_user():
    if request.method == 'POST':
        # Check login is valid
        email = request.form['email']
        password = request.form['hashed']

        if User.is_login_valid(email, password):
            # email and password are valid
            session['email'] = email
            return redirect(url_for('.user_alerts'))
            # redirects user to their login page ".user_alerts"
            # url_for redirects to a url connected to a specific method, in this case the user_alerts method
        else:
            # email and password are not valid
            raise UserErrors.LoginNotValidError('Your email or password are incorrect. Please re-enter your login details or register for a new account.')
            return render_template('user/login.html')

    return render_template('user/login.html') # Here the request method is GET: Send user to login page




@user_blueprint.route('/register')
def register_user():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    pass


@user_blueprint.route('/logout')
def logout_user():
    pass

@user_blueprint.route('check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass