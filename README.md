# Exams Microservice

[![CI](https://github.com/Ubademy-G3/exams.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/exams.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/exams.service/branch/main/graph/badge.svg?token=A3547H62WC)](https://codecov.io/gh/Ubademy-G3/exams.service)

# File Structure:
```tree
├── application
│   ├── controllers
│   │   ├── exam_solution_controller.py
│   │   ├── exam_template_controller.py
│   │   ├── __init__.py
│   │   ├── question_solution_controller.py
│   │   └── question_template_controller.py
│   ├── __init__.py
│   ├── serializers
│   │   ├── exam_solution_serializer.py
│   │   ├── exam_template_serializer.py
│   │   ├── __init__.py
│   │   ├── question_solution_serializer.py
│   │   └── question_template_serializer.py
│   ├── services
│   │   ├── auth.py
│   │   └── __init__.py
│   └── use_cases
│       ├── exam_solution
│       │   ├── create.py
│       │   ├── delete.py
│       │   ├── get.py
│       │   ├── __init__.py
│       │   └── update.py
│       ├── exam_template
│       │   ├── create.py
│       │   ├── delete.py
│       │   ├── get.py
│       │   ├── __init__.py
│       │   └── update.py
│       ├── __init__.py
│       ├── question_solution
│       │   ├── create.py
│       │   ├── delete.py
│       │   ├── get.py
│       │   ├── __init__.py
│       │   └── update.py
│       └── question_template
│           ├── create.py
│           ├── delete.py
│           ├── get.py
│           ├── __init__.py
│           └── update.py
├── deploy
│   └── heroku-entrypoint.sh
├── docker-compose.yml
├── Dockerfile
├── domain
│   ├── exam_solution_model.py
│   ├── exam_template_model.py
│   ├── __init__.py
│   ├── question_solution_model.py
│   └── question_template_model.py
├── exceptions
│   ├── auth_exception.py
│   ├── http_exception.py
│   ├── __init__.py
│   └── ubademy_exception.py
├── heroku.yml
├── infrastructure
│   ├── db
│   │   ├── database.py
│   │   ├── exam_solution_schema.py
│   │   ├── exam_template_schema.py
│   │   ├── __init__.py
│   │   ├── question_solution_schema.py
│   │   └── question_template_schema.py
│   ├── __init__.py
│   └── routes
│       ├── exam_solution_outside_router.py
│       ├── exam_solution_router.py
│       ├── exam_template_router.py
│       ├── __init__.py
│       ├── question_solution_router.py
│       └── question_template_router.py
├── LICENSE
├── logging.ini
├── main.py
├── monitoring
│   └── datadog.yml
├── persistence
│   ├── __init__.py
│   └── repositories
│       ├── exam_solution_repository_postgres.py
│       ├── exam_template_repository_postgres.py
│       ├── __init__.py
│       ├── question_solution_repository_postgres.py
│       └── question_template_repository_postgres.py
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    ├── infrastructure
    │   └── __init__.py
    ├── __init__.py
    ├── test_exam_solutions.py
    ├── test_exam_templates.py
    └── test_question_templates.py
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Environment variables

To run this application you need to define the following environment variables:

```
API_KEY = "YOUR_EXAMS_SERVICE_APIKEY"
```

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `examsservice_web`: Web Service
* `examsservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```

## Down services and remove containers, networks, volumes and images created by 'up'

```docker-compose down```

## To run tests

```docker-compose exec web pytest .```


You can try it out at <https://staging-exams-service.herokuapp.com/docs>
