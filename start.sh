#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -it --rm -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}
