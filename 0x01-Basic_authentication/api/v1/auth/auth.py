#!/usr/bin/env python3
"""
Module contains the Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class definition
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method returns None. request is the Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method returns None. request is the Flask request object.
        """
        return None
