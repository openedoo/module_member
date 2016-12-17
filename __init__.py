from openedoo.core.libs import *
import json
import module_member
#from module_member import registration,activation
from openedoo.core.libs.tools import *
from openedoo.core.libs.auth import login as user_login
from openedoo.core.libs.auth import read_session, logout as user_logout


modul_member = Blueprint('member', __name__)

@modul_member.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@modul_member.route('/register', methods=['POST','GET'])
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
    try:
        if (username or email or password) is None:
            abort(401)
        payload = module_member.registration(username,password,email,name,phone)
        #payload = {'message':'registration successful'}
        payload = json.dumps(payload)
        resp = Response(payload, status=200, mimetype='application/json')
        return resp
    except Exception as e:
        abort(401)

@modul_member.route('/delete', methods=['GET','POST'])
@read_session
def delete():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
    else:
        user_id = request.args.get('id')
    return delete(user_id=user_id)

@modul_member.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
        module_member.object.by_id(user_id=user_id)
        #member.object.order_by(user_id=user_id)
        return module_member.object.show_data()

@modul_member.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        load_json = json.loads(request.data)

@modul_member.route('/activation/<key>',methods=['GET'])
def activation(key):
    aktivasi = json.dumps(module_member.activation(key))
    resp = response(aktivasi, status=200, mimetype='application/json')
    return resp

@modul_member.route('/password', methods=['POST','GET'])
@read_session
def password():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        edit = json.dumps(module_member.edit_password(
            user_id=load_json['user_id'],
            password_old=load_json['old_password'],
            password_new=load_json['new_password'],
            password_confirm=load_json['confirm_password']
        ))
        resp = Response(edit, status=200, mimetype='application/json')

    return resp

@modul_member.route('/login', methods=['POST', 'GET'])
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

@modul_member.route('/logout')
def logout():
    log = json.dumps(user_logout())
    resp = Response(log, status=200, mimetype='application/json')
    return resp
