import jwt
import datetime

SECRET_KEY = "mysecret"

# function to get jwt token
def get_jwt_token(username):
    payload = {
        "sub": username,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

#function to decode jwt token
def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token expired")
        return None
    except jwt.InvalidTokenError as e:
        print(f"Invalid token error: {e}")
        return None
    except Exception as e:
        print(f"Other decoding error: {e}")
        return None
