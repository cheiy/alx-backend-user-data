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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        result = []
        for paths in excluded_paths:
            if paths[:-1] == path or paths == path or paths == path[:-1]:
                result.append("False")
            else:
                result.append("True")
        if "False" in result:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        Method returns None. request is the Flask request object.
        """
        if request is None:
            return None
        if request.headers.get("Authorization") is None:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method returns None. request is the Flask request object.
        """
        return None
