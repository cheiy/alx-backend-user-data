#!/usr/bin/env python3
"""
Module contains the basic_auth class
"""
from api.v1.auth.auth import Auth
import base64


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
