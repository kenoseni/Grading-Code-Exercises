#!/bin/bash

# initializing variables, here, $1 is the first argument from cli
env=$1
file=""
fails=""

# conditional statement to check what was passed with the start script
if [[ "${env}" == "stage" ]]; then
    file="docker-compose-dev.yml"
elif [[ "${env}" == "dev" ]]; then
    file="docker-compose-dev.yml"
elif [[ "${env}" == "prod" ]]; then
    file="docker-compose-prod.yml"
else
    echo "USAGE: sh test.sh environment_name"
    echo "* environment_name: must either be 'dev', 'stage', or 'prod'"
    exit 1
fi

# inspect function that calculates the number of failures
inspect() {
    if [ $1 -ne 0 ]; then
        fails="${fails} $2"
    fi
}

docker-compose -f $file run users python manage.py test
# 
inspect $? users
# docker-compose -f $file run users flake8 project
# 
# inspect $? users-lint
# 
if [[ "${env}" == "dev" ]]; then
    docker-compose -f $file run client npm test -- --coverage
    inspect $? client
    npm test
    inspect $? e2e
    
else
    npm run test
    inspect $? e2e
fi

# check if string in variable fails is not empty then echo its content
if [ -n "${fails}" ]; then
    echo "Test failed: ${fails}"
    exit 1
else
    echo "Test passed!"
    exit 0
fi
