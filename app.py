from flask_jwt_extended import create_access_token, jwt_required,set_access_cookies,unset_jwt_cookies,JWTManager
from flask import Flask,render_template,jsonify, request
import os

jwt = JWTManager()

app = Flask(__name__)
jwt.init_app(app)
app.config['JWT_SECRET_KEY'] = os.urandom(24)
app.config['JWT_TOKEN_LOCATION'] = ['headers','query_string']
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

@app.route('/')
def index():
    
    AccountName='bob'
    access_token = create_access_token(identity=AccountName)
    
    return jsonify({'login_status':'seccess','jwt':access_token})


# http://127.0.0.1:5000/helloJwt?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNzY5ODU4MCwianRpIjoiYTNjM2E0MmEtMTE5Zi00YzE5LWJjN2EtZmEwY2U4ZmI5ODQyIiwibmJmIjoxNjE3Njk4NTgwLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiZXhhbXBsZV91c2VyIiwiZXhwIjoxNjE3Njk5NDgwfQ.2krXs3rFhYj1xw4kRxkD_OnnSKcXPbQZeY5DxYzQW3o
@app.route('/helloJwt')
@jwt_required()
def jwtTest():
    return 'jwt test success.'



if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=8888)    

