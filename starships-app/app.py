from chalice import Chalice, AuthResponse, UnauthorizedError
from chalicelib import auth
from chalicelib.swapidev import Swapidev
import logging

app = Chalice(app_name="starships-app")
app.debug = False
users_db = {"user1": "12345"}
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/login", methods=["POST"], cors=True)
def login():
    request = app.current_request
    username = request.json_body.get("username")
    password = request.json_body.get("password")

    if username in users_db and users_db[username] == password:
        token = auth.get_jwt_token(username)
        logger.info(f"Generated JWT for {username}: {token}") 
        return {"token": token}
    else:
        raise UnauthorizedError("Invalid username or password")

@app.authorizer()
def jwt_auth(auth_request):
    token = auth_request.token
    if not token:
        raise UnauthorizedError("No token provided")
    if token.startswith("Bearer "):
        token = token[7:]
    
    decoded = auth.decode_jwt_token(token)
    if decoded is None:
        raise UnauthorizedError("Invalid token")
    
    return AuthResponse(routes=["*"], principal_id=decoded["sub"])

@app.route("/starships", methods=["GET"], authorizer=jwt_auth, cors=True)
def get_starships():
    params = app.current_request.query_params or {}
    swapidev = Swapidev()
    starships = swapidev.get_starships(**params)
    return {"starships": starships}

@app.route("/manufacturers", methods=["GET"], authorizer=jwt_auth, cors=True)
def get_manufacturer():
    
    swapidev = Swapidev()
    manufacturers = swapidev.get_manufacturers()
    return {"manufacturers": manufacturers}
