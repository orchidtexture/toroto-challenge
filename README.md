# toroto-challenge Docker Compose

|Service| Service Name | Port |
|---|---|---|
| postgres | toroto_postgres | 5432 |
| backend | toroto-challenge_backend | 8000 |
| frontend | toroto-challenge_frontend | 3000 |

## Setting everything up

1. Install docker https://www.docker.com/get-docker
3. Install docker-compose https://docs.docker.com/compose/install/
4. cd into root directory
5. Start the **docker-compose** service.

## Basic Usage

- Build all services `docker-compose up --build`

- Start all services `docker-compose up`

- Stop all services `docker-compose stop`

- Open the shell `docker-compose exec backend /bin/sh`
