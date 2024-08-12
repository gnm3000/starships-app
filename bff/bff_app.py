from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

if "DOCKER_COMPOSE" in os.environ:
    BACKEND="starships-app"
else:
    BACKEND="localhost"

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/bff/starships")
async def get_starships(request: Request):
    token = request.headers.get('Authorization')
    headers = {'Authorization': token}

    manufacturer = request.query_params.get('manufacturer')
    url = f'http://{BACKEND}:8000/starships'
    if manufacturer:
        url += f'?manufacturer={manufacturer}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching starships")

@app.get("/bff/manufacturers")
async def get_manufacturers(request: Request):
    token = request.headers.get('Authorization')
    headers = {'Authorization': token}

    response = requests.get(f'http://{BACKEND}:8000/manufacturers', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching manufacturers")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)