#!/bin/bash

python3 DockerClient.py -U $FINDING_CHESS_USERNAME -P $FINDING_CHESS_PASSWORD -S http://135.148.27.107/

wait -n

exit $?