#!/bin/bash
docker container kill horizon-dns

sleep 1

docker run -d \
	--rm \
	-p 443:443 \
	-p 53:53/udp \
	-p 53:53/tcp \
	--name horizon-dns \
	horizon-dns
