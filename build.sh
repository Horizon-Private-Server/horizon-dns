#!/bin/bash

# Reset the docker image
#docker rmi dnas-test
# Pass in the server IP
docker build --tag dnas-test --build-arg serverip=${1} .
