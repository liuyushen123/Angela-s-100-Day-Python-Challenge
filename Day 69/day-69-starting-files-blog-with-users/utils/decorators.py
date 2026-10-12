# decorators.py
from functools import wraps
from flask import abort
from flask_login import current_user
from model.blog_post import BlogPost


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            return abort(403)
        return func(*args, **kwargs)

    return wrapper


def authenticated_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)
        return func(*args, **kwargs)

    return wrapper


def author_or_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)

        post = BlogPost.get_post_by_id(kwargs.get("post_id"))
        if post is None:
            return abort(404)

        if current_user.id != post.author_id and not current_user.is_admin:
            return abort(403)

        return func(*args, **kwargs)

    return wrapper


def author_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)

        post = BlogPost.get_post_by_id(kwargs.get("post_id"))
        if post is None:
            return abort(404)

        if current_user.id != post.author_id:
            return abort(403)

        return func(*args, **kwargs)

    return wrapper
