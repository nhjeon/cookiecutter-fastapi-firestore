# {{ cookiecutter.project_name }}

&nbsp;[![Python Version: 3.7.4](https://badgen.net/badge/python/3.7.4/blue)](https://docs.python.org/3.7.4/)

&nbsp;[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)


## Getting Started


### Installation

```sh
$ make
```

## Test

```sh
$ make check
$ make test
```


## Run

``` sh
GOOGLE_APPLICATION_CREDENTIALS=./serviceAccount.json PYTHONPATH=./app python ./run.py
or
make run
```

## Docker

```
make requirements
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage
```


## Requirements

<!-- TODO: Describe stack of this project -->

* [Pipenv](https://github.com/pypa/pipenv) - 의존성 관리
* FastAPI