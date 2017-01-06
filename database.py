from openedoo import db
from openedoo import config

database_prefix = config.database_prefix

class OD_users(db.Model):
	__tablename__ = '{db_prefix}_user'.format(db_prefix=database_prefix)
	user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	username = db.Column(db.String(16), unique=True)
	password = db.Column(db.Text())
	access_token = db.Column(db.Text())
	public_key = db.Column(db.Text())
	private_key = db.Column(db.Text())
	status = db.Column(db.Integer)
	role = db.Column(db.String(64))
	created = db.Column(db.DateTime())
	last_login = db.Column(db.DateTime())
	user_profile = db.Column(db.Text())
	def __init__(self,username,password,access_token,public_key,private_key,status,role,created,last_login,user_profile):
		self.username = username
		self.password = password
		self.access_token = access_token
		self.public_key = public_key
		self.private_key = private_key
		self.status = status
		self.role = role
		self.created = created
		self.last_login = last_login
		self.user_profile = user_profile
class OD_roles(db.Model):
	__tablename__ = '{db_prefix}_user_role'.format(db_prefix=database_prefix)
	role_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	role = db.Column(db.String(64))
	role_status = db.Column(db.Text)
	def __init__(self,role,max_device,role_status):
		self.role = role
		self.role_status = role_status
