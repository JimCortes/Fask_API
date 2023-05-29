from flask import Flask, jsonify, request, abort
from methods import Token, Restricted
from convert import CidrMaskConvert, IpValidate

app = Flask(__name__)
login = Token()
protected = Restricted()
convert = CidrMaskConvert()
validate = IpValidate()

def health_check():
    response = {"response": "OK"}
    return jsonify(response), 200

def authenticate(func):
    def valid_jwt(*args, **kwargs):
        token = request.headers.get('Authorization')
        if protected.access_data(token):
            return func(*args, **kwargs)
        else:
            abort(401)
    valid_jwt.__name__ = func.__name__ 
    return valid_jwt

# Just a health check
@app.route("/")
def url_root():  
    return health_check()
# Just a health check
@app.route("/_health")
def url_health():
    return health_check()

# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    user_name = request.form['username']
    password = request.form['password']
    # This database data is here just for you to test, please, remember to define your own DB
    # You can test with username = admin, password = secret  
    # This DB has already a best practice: a salt value to store the passwords
    token = login.generate_token(user_name, password) 
    if token:
        return jsonify({"data": token})
    else:
        abort(401)

# e.g. http://127.0.0.1:8000/cidr-to-mask?value=8
@app.route("/cidr-to-mask")
@authenticate
def url_cidr_to_mask():
    cidr = request.args.get('value')
    mask = convert.cidr_to_mask(cidr)
    return  jsonify({"function": "cidr_to_ask", "input": cidr, "output": mask})

# e.g. http://127.0.0.1:8000/mask-to-cidr?value=255.0.0.0

@app.route("/mask-to-cidr")
@authenticate
def url_mask_to_cidr():  
    mask = request.args.get('value')
    cidr = convert.mask_to_cidr(mask)
    return jsonify({"function": "mask_to_cidr", "input": mask, "output": cidr})



