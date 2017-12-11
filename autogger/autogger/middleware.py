"""
	Contains the required middleware stuff
"""
from django.utils.deprecation import MiddlewareMixin



class JwtAuthorizationMiddleware(MiddlewareMixin):
    """
    Middleware to authenticate the jwt token from request header.
    """

    def __init__(self, get_response):
        self.get_response = get_response
