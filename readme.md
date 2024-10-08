## Technical Challenge: full-stack application

### Introduction

Welcome to the technical challenge of implementing a full-stack application using the StarWars API. 

Video Available: https://streamable.com/18rvly


### Start using Docker 
To start, clone the repository
```
git clone git@github.com:gnm3000/starships-app.git
```

If you have Docker Compose and Docker installed on your machine, to execute in this way, we use the file docker-compose.yml


```
docker compose up --build
```
Then go to localhost:3000

### Credentials
Use user: "user1" password: "12345"



### Prerequisites for Installation

This project is using:
- NextJS 14.x latest
- Docker compose + Docker
- npm latest
- Python 3.10

### Structure

You will find two folders:
- starship-frontend:  a NextJS 14.x app
- starships-app:  the backend of the application using Python Chalice framework
- bff: This is Backend-for-Frontend (The one NextJS is using)



This command will run two Dockerfiles
- Frontend: starship-frontend/Dockerfile: building NextJS app using NodeJS
- Backend: starships-app/Dockerfile; running a Chalice app in a local mode


### Backend Documentation

Using Chalice, Framework for AWS Lambda development
Endpoints:
- POST /login: using username and password it generates a JWT token
- GET /starships: Return all starships that can be filtered using parameters.
-- GET /starships?manufacturer=Corellian Engineering Corporation&model=CR90 corvette
- GET /manufacturers: Return all manufacturers available in the starships endpoint with cache

### Installation

Install NextJS for the Frontend:

git clone git@github.com:gnm3000/starships-app.git

 - cd starship-frontend
 - npm install
 - npm run dev (http://localhost:3000)

Install Chalice Framework for the Backend:PYTHON
- cd starships-app
- create a virtualenv
- pip install -r requirements.txt
- export PYTHONPATH=$(pwd)
- pytest
- chalice local (Serving on http://127.0.0.1:8000)

Install FastAPI for (BFF) Backend for Frontend (running FastAPI)
- cd bff
- create virtualenv
- pip install -r requirements.txt
- python bff_app.py

### Functional Requirements

This application has:
- A login with username and password
- A frontend with a table and a select as a filter with manufacturers
- You can select one specific to filter results

### Testing

- Backend (starships-app): using pytest for Swapidev class and for Chalice testing
- You can do 

### Deployment
- Localhost using docker-compose.





### Security Considerations
- The application has just one user:
-- username: user1
-- password: 12345

### Conclusion

When it's up, you can access to the frontend (:3000), login and visualize in a table starships and filter by manufacturer. The backend (starships-app) support filtering for more fields, but the backend for frontend (bff folder) use just manufacturer.



