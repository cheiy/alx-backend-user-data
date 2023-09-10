#!/usr/bin/env python3
"""
Module contains the basic_auth class
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class inherits from Auth to perform authentication
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Function extracts valid base64 strings
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.split(" ")[0] != "Basic":
            return None
        else:
            return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Function decodes base64 strings
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """
        Function returns the user email and password from the Base64 decoded
        value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Method returns the User instance based on his/her email and password
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            user_list = User.search({'email': user_email})
        except Exception:
            return None
        for user in user_list:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method gets the current user"""
        try:
            auth_header = self.authorization_header(request)
            enc = self.extract_base64_authorization_header(auth_header)
            dec = self.decode_base64_authorization_header(enc)
            email, pwd = self.extract_user_credentials(dec)
            return self.user_object_from_credentials(email, pwd)
        except Exception:
            return None
