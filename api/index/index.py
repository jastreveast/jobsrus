# index will only send html vue file 
from flask import Blueprint, current_app, render_template


index_bp = Blueprint(
    'index_bp',
    __name__,
   
)

@index_bp.route('/')
def index():
    return current_app.send_static_file('index.html')
