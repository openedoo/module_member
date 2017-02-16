from openedoo.core.libs import *
import json
import model_member
#from module_member import registration,activation
from openedoo.core.libs.tools import *
from auth import login as user_login
from auth import read_session, logout as user_logout


module_member = Blueprint('member', __name__)

@module_member.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@module_member.route('/register', methods=['POST','GET'])
def add():
    try:
        if request.method == 'POST':
            load_json = json.loads(request.data)
            username = load_json['username']
            password = load_json['password']
            email = load_json['email']
            name = load_json['name']
            phone = load_json['phone']
    except Exception as e:
        abort(500)
    #try:
    #    if (username or email or password) is None:
    #        abort(401)
    payload = model_member.registration(username,password,email,name,phone)
        #payload = {'message':'registration successful'}
    payload = json.dumps(payload)
    resp = Response(payload, status=200, mimetype='application/json')
    return resp
    #except Exception as e:
     #   abort(401)

@module_member.route('/delete', methods=['GET','POST'])
@read_session
def delete():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
    else:
        user_id = request.args.get('id')
    return delete(user_id=user_id)

@module_member.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
        model_member.object.by_id(user_id=user_id)
        #member.object.order_by(user_id=user_id)
        return model_member.object.show_data()

@module_member.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        load_json = json.loads(request.data)

@module_member.route('/activation/<key>',methods=['GET'])
def activation(key):
    aktivasi = json.dumps(model_member.activation(key))
    resp = response(aktivasi, status=200, mimetype='application/json')
    return resp

@module_member.route('/password', methods=['POST','GET'])
@read_session
def password():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        edit = json.dumps(model_member.edit_password(
            user_id=load_json['user_id'],
            password_old=load_json['old_password'],
            password_new=load_json['new_password'],
            password_confirm=load_json['confirm_password']
        ))
        resp = Response(edit, status=200, mimetype='application/json')

    return resp

@module_member.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            load_json = json.loads(request.data)
            check_login = user_login(load_json['username'] ,load_json['password'])
            log = json.dumps(check_login)
            resp = response(log, status=200, mimetype='application/json')
            return resp
    except Exception as e:
        abort(500)

@module_member.route('/logout')
def logout():
    log = json.dumps(user_logout())
    resp = Response(log, status=200, mimetype='application/json')
    return resp

#TESEEEETTTT
