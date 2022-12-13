import pytest
from pathlib import Path
from app.entities.user.value_objects import *


class EmailTest:
    def test_email_without_at(self):
        with pytest.raises(ValueError):
            Email('testgmail.com')

    def test_email_with_spaces(self):
        with pytest.raises(ValueError):
            Email('test @gmail.com')

    def test_email_without_username(self):
        with pytest.raises(ValueError):
            Email('@gmail.com')

    def test_email_without_domain(self):
        with pytest.raises(ValueError):
            Email('test@')

    def test_email_with_wrong_domain(self):
        with pytest.raises(ValueError):
            Email('test@gmailcom')

    def test_email(self):
        Email('test@gmail.com')


class PasswordTest:
    def test_password_without_digits(self):
        with pytest.raises(ValueError):
            Password('TestPassword!')

    def test_password_without_uppercase(self):
        with pytest.raises(ValueError):
            Password('testpassword1!')

    def test_password_without_lowercase(self):
        with pytest.raises(ValueError):
            Password('TESTPASSWORD1!')

    def test_password_without_special_characters(self):
        with pytest.raises(ValueError):
            Password('TestPassword1')

    def test_password_less_than_8_characters(self):
        with pytest.raises(ValueError):
            Password('Test1!')

    def test_password_more_than_32_characters(self):
        with pytest.raises(ValueError):
            Password('TestPasswordTestPasswordTestPassword1!')

    def test_password(self):
        Password('TestPassword1!')


class PostTest:
    def test_post(self):
        Post.BACKEND

    def test_post_2(self):
        Post('backend')

    def test_post_wrong(self):
        with pytest.raises(ValueError):
            Post('test')

    def test_post_wrong_type(self):
        with pytest.raises(ValueError):
            Post(1)


class UserNameTest:
    def test_username(self):
        with pytest.raises(ValueError):
            UserName('test')

    def test_username_not_str(self):
        with pytest.raises(TypeError):
            UserName(123)

    def test_username_short(self):
        with pytest.raises(ValueError):
            UserName('te')

    def test_username_long(self):
        with pytest.raises(ValueError):
            UserName('testtesttesttesttesttesttest')

    def test_username_with_spaces(self):
        with pytest.raises(ValueError):
            UserName('test test')

    def test_username_start_digit(self):
        with pytest.raises(ValueError):
            UserName('1test')

    def test_username_dentifier(self):
        with pytest.raises(ValueError):
            UserName('number1')

    def test_username_special_characters(self):
        with pytest.raises(ValueError):
            UserName('test-test')

    def test_username_special_characters_2(self):
        with pytest.raises(ValueError):
            UserName('test@test')

    def test_username_with_digit(self):
        with pytest.raises(ValueError):
            UserName('1')