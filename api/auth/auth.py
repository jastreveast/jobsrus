from flask import Blueprint, current_app, render_template


auth_bp = Blueprint(
    'auth_bp',
    __name__,
   
)

@auth_bp.route('/')
def auth():
    pass