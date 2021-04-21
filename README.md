# BLUEVOYANT

## Pre-requisites
Python3.7 or Higher
1. [python3](https://www.python.org/downloads/mac-osx/)
2. [Docker](https://docs.docker.com/get-docker/)
3. [Docker Compose](https://docs.docker.com/compose/install/)

## Get Started
1. Git Clone into desired directory
2. Change into directory with cloned code.
3. Update `.env` file with `MARVEL_API_PUBLIC_KEY`, `MARVEL_API_PRIVATE_KEY`
    - Will leave mine in case.
3. Get Docker up and running: `docker-compose up -d --build`
4. Check Docker is up and running. Go to http://localhost:5004/ping
5. Check Status of DB: `docker-compose exec api python manage.py check_status`
6. Create DB: `docker-compose exec api python manage.py recreate_db`
7. Seed DB: `docker-compose exec api python manage.py seed_db`
8. Check Characters has been seeded.
    * Go to http://localhost:5004/characters
9. Head to http://localhost:5004/characters/spectrum/associated 
    - Here you will receive a record of all marvel characters Spectrum has ever encountered.

## NOTE:
1. Error Handling is non-existent here. I built a working prototype for a working use case. 
    * I would love to handle incorrect user inputs, tests, etc.
2. This was very fun. 

### Thank you. 
