from flask import Blueprint,render_template

main = Blueprint('main',__name__,template_folder="templates")

@main.route('/',methods=['GET'])
def home():
    return render_template('index.html')