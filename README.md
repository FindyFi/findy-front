# FIndy front-end
Front end for Findynet customers

## Prerequisite 

- Unix shell
- Python 3.6 ([pyenv recommended](https://github.com/pyenv/pyenv#installation))
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (If you run locally)
- PostgreSQL
- [Docker](https://www.docker.com/) (If you run via docker)


## How to run locally

Clone repository
```sh
git clone https://github.com/FindyFi/findy-front.git
cd findy-front
```

Update `pool_transactions_genesis` based on which ledger you want to connect

Setup a standard local PostgreSQL with database `findytestfrontdb` with user `postgres` and no DB password, in case you want to connect to an external db you can set DB_HOST, DB_NAME, DB_USER and DB_PASSWORD in .env file.

Add a table `users` with columns `email` and `password`. Also add a record in which password is hashed using SHA256. You can use the provided script below.


```sql
-- Create 'users' table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(255),
    password VARCHAR(64)
);

-- Insert a record into 'users' table with user: 'test@findy.fi' and password: 'test'
INSERT INTO users (email, password) VALUES ('test@findy.fi', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08');
```


Create `.env` file at the root of project and add `TRUSTEE_SEED` and `JWT_SECRET` value as enviornment variables.
```sh
echo "TRUSTEE_SEED=000000000000000000000000Trustee1\nJWT_SECRET=secret" > .env
```

Create and activate python virtual enviornment 
```sh
virtualenv --python=python3.6 venv
source venv/bin/activate
```

Install dependencies and run the front end
```sh
pip install -r server/requirements.txt
source .env 
./start.sh $TRUSTEE_SEED $JWT_SECRET
```

## How to run via docker

Clone repository
```sh
git clone https://github.com/FindyFi/findy-front.git
cd findy-front
```

Update `pool_transactions_genesis` based on which ledger you want to connect

Create `.env` file at the root of project and add `TRUSTEE_SEED` value.

```sh
echo "TRUSTEE_SEED=000000000000000000000000Trustee1" > .env
```

Build and run docker containers
```sh
docker-compose up
```
