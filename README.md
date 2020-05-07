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
5. Build and start all services `docker-compose up --build`
6. Apply all initial migrations `docker-compose run backend python manage.py migrate`
7. Go to http://localhost:3000/

## Basic Usage

- Build all services `docker-compose build`

- Start all services `docker-compose up`

- Stop all services `docker-compose stop`

- Open the shell `docker-compose exec backend /bin/sh`

## API Usage Example

1. Register as an user:
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/users/staff/register/
    - method: POST
    - body: (Select raw and JSON options)
    ```json
    {
        "email": "your email",
        "password": "your password",
        "first_name": "your first name",
        "last_name": "your last name"
    }
    ```
    ![register example](register_example.png)
2. Copy the auth token from the response
3. Create a new request for subscribers list:
    - header: 
        - `Key = Authorization` 
        - `value = Token {paste_token}`
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/subscribers/
    - method: GET

    ![subscribers list example](subscribers_list_example.png)

## Endpoints

1. Register staff user
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/users/staff/register/
    - method: `POST`
    - Authentication: non required
    - body:
    ```json
    {
        "email": "your email",
        "password": "your password",
        "first_name": "your first name",
        "last_name": "your last name"
    }
    ```
2. Retrieve, update and destroy staff user
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/users/    
    - method: `GET/PATCH/DELETE`
    - Authentication: required
    - body:
    ```json
    {
        "email": "your updated email",
        "first_name": "your updated first name",
        "last_name": "your updated last name"
    }
    ```
3. User Login
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/users/login/    
    - method: `POST`
    - Authentication: required
    - body:
    ```json
    {
        "email": "your email",
        "password": "your password"
    }
    ```
4. Retrieve subscribers list
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/subscribers/    
    - method: `GET`
    - Authentication: required

5. Create new subscriber
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/subscribers/new/   
    - method: `POST`
    - Authentication: required
    - body:
    ```json
    {
        "email": "subscriber's email",
        "first_name": "subscriber's first name",
        "last_name": "subscriber's last name",
        "co2_tons_per_year": "10.00"
    }
    ```
6. Retrieve, update and destroy subscriber
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/subscribers/{subscriber_id}/  
    - method: `GET/PATCH/DELETE`
    - Authentication: required
    - body:
    ```json
    {
        "email": "ssubscriber's updated email",
        "first_name": "subscriber's updated first name",
        "last_name": "subscriber's updated laste name",
        "co2_tons_per_year": "9.00",
        "has_subscription": true,
        "subscription": {
            "monthly_fee": "6.00",
            "co2_tons_per_month": "0.40"
        }
    }
    ```
    Note: The has_subscription=true is required in order to update the subscription. 
7. Create new subscription
    - url: https://secret-shelf-40223.herokuapp.com/api/v1/subscriptions/  
    - method: `POST`
    - Authentication: required
    - body:
    ```json
    {
        "subscriber_id": "subscriber's id"
    }
    ```

