
import hashlib
import jwt
import mysql.connector

secret_key = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

data_base = mysql.connector.connect(
        host='sre-bootcamp.czdpg2eovfhn.us-west-1.rds.amazonaws.com',
        user='secret',
        password='jOdznoyH6swQB9sTGdLUeeSrtejWkcw',
        database='bootcamp_tht'  
    )



class Token:
    def generate_token(self, user_name, input_password):
        cursor = data_base.cursor()
        cursor.execute(f"SELECT salt, password, role from users where username ='{user_name}';")
        query = cursor.fetchone()
        if len(query):
            salt, password, role = query
            hash_pass=hashlib.sha512((input_password+salt).encode()).hexdigest()
            if hash_pass==password:
                encode_jwt = jwt.encode({"role": role}, secret_key, algorithm='HS256')
                return encode_jwt
        return False
    
class Restricted:
    def access_data(self, authorization): 
        try:
            decode_jwt = jwt.decode(authorization.replace('Bearer', ''), secret_key, algorithms='HS256')
            if 'role' in decode_jwt:
                return 'You are under protected data'
        except:
            return False

