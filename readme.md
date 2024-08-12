## Technical Challenge: full-stack application

### Introduction

Welcome to the technical challenge of implementing a full-stack application using the StarWars API. 


### Prerequisites

This project is using:
- NextJS 14.x latest
- Docker compose + Docker
- npm latest
- python 3.10

### Structure

You will find two folders:
- starship-frontend:  a NextJS 14.x app
- starships-app:  the backend of the application using Python Chalice framework

docker-compose.yml file is for run the complete project using docker compose

Command using docker compose

```
docker compose up --build
```

This command will run two Dockerfiles
- Frontend: starship-frontend/Dockerfile: building NextJS app using NodeJS
- Backend: starships-app/Dockerfile; running a Chalice app in a local mode


### Backend Documentation

Using Chalice, Framework for AWS lambdas development
Endpoints:
- POST /login: using username and password it generated a JWT token
- GET /starships: Return all starships that could be filtered using parameters.
-- GET /starships?manufacturer=Corellian Engineering Corporation&model=CR90 corvette
- GET /manufacturers: Return all manufacturers available in starships endpoint with cache


### Instalation

Frontend:
git clone git@github.com:gnm3000/starships-app.git
 - cd starship-frontend
 - npm install
 - npm run dev (http://localhost:3000)

Backend:
- cd starships-app
- create a virtualenv
- pip install -r requirements.txt
- chalice local (Serving on http://127.0.0.1:8000)

Backend for Frontend (running FastAPI)
- cd bff
- create virtualenv
- pip install -r requirements.txt
- port 5000

### Functional Requirements

This application has:
- A login with username and password
- A frontend with a table and a select as a filter with manufacturers
- You can select one specific to filter results

### Testing

- Backend: using pytest for Swapidev Class and for Chalice testing

### Deployment
- The application can run on localhost using docker compose: 
```
docker compose up --build
```





### Security Considerations
- The application just have one user:
-- username: user1
-- password: 12345

### Conclusion

When it's up, you can access to the frontend (:3000), login and visualize in a table starships and filter by manufacterer. The backend (starships-app) support filtering for more fields, but the backend for frontend (bff folder) use just manufacterer.




### Instructions

1. docker compose up --build

2. user: user1 password: 12345
