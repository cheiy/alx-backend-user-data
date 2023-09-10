#!/usr/bin/env python3
"""
Module contains the basic_auth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Class inherits from Auth to perform authentication
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.split(" ")[0] != "Basic":
            return None
        else:
            return authorization_header.split(" ")[1]
