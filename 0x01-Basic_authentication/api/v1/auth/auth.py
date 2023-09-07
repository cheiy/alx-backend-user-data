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
        """
        standardise the path to remove slashes if the path already
        has slashes
        """
        if path[-1] == "/":
            path = path[:-1]
        for paths in excluded_paths:
            if paths[-1] == "/":
                """
                standardise the paths in excluded_paths to
                remove slashes if they already have slashes
                """
                paths = paths[:-1]
                if paths == path:
                    return False
                else:
                    return True
            else:
                return True

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
