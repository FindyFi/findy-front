# FIndy front-end
Front end for Findynet customers

## Prerequisite 

- Unix shell
- Python 3.6 ([pyenv recommended](https://github.com/pyenv/pyenv#installation))
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (If you run locally)
- [Docker](https://www.docker.com/) (If you run via docker)


## How to run locally

Clone repository
```sh
git clone https://github.com/FindyFi/findy-front.git
cd findy-front
```

Update `pool_transactions_genesis` based on which ledger you want to connect

Create `.env` file at the root of project and add `TRUSTEE_SEED` value and `JWT_SECRET` value
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

## How to run in a docker

Clone repository
```sh
git clone https://github.com/FindyFi/findy-front.git
cd findy-front
```

Update `pool_transactions_genesis` based on which ledger you want to connect

Create `.env` file at the root of project and add `TRUSTEE_SEED` value and `JWT_SECRET` value

```sh
echo "TRUSTEE_SEED=000000000000000000000000Trustee1\nJWT_SECRET=secret" > .env
```

Build and run docker container
```sh
docker build -f ./Dockerfile -t findy_front .
docker run -itd -p 9000:80 findy_front
```
