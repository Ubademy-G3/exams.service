# Exams Microservice

[![CI](https://github.com/Ubademy-G3/exams.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/exams.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/exams.service/branch/main/graph/badge.svg?token=A3547H62WC)](https://codecov.io/gh/Ubademy-G3/exams.service)

# File Structure:
```tree
├── main.py
├── src
│   ├── infrastructure
│   │   ├── db
│   │   │   ├──  exam_shema.py 
│   │   │   └──  database.py 
│   │   ├── routes
│   │   │   └──  exams.py
│   ├── persistence
│   │   └── repositories
│   │       └── exam_repository_postgres.py
│   ├── application
│   │   ├── controllers
│   │   │   └── 
│   │   ├──serializers
│   │   │   └── 
│   │   └── useCases
│   │       └── 
│   └── domain
│       ├── exam_model.py
│       └── exam_repository.py
├── monitoring
├── deploy
└── tests
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `examsservice_web`: Web Service
* `examsservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```
