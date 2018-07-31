import uuid

from src.common.database import Database
import src.models.users.errors as UserErrors
from src.common.utils import Utils



class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        '''
        This method verifies that an email/password combo (as sent by the site forms) is valid or not.
        Checks that the email exists, and that the password associated to that email is correct.
        :param email: The user's email
        :param password: A sha512 hashed password (encryption)
        :return: True if valid, False otherwise
        '''
        user_data = Database.find_one('users', {'email': email}) # Password in sha512 -> pbkdf2_sha512 AND looks in users collection in price_alert database and checks for json file email
        if user_data is None:
            raise UserErrors.UserNotExistsError('This user does not exist.')
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError('This password is wrong.')

        return True

