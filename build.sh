#!/bin/bash

# Reset the docker image
#docker rmi dnas-test
# Pass in the server IP
docker build --tag dnas-test --build-arg gateip=${1} --build-arg prodip=${2} --build-arg betaip=${3} .
