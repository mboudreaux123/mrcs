#!/bin/bash

## This bash script is to be executed at system boot by a deamon,
## allowing the execution of scripts or programs as the system boots.
## Currently the script will download the latest robot code from a
## git repository and execute the code afterwards.

CURRENT_DIR=$(dirname $(readlink -f $0))
SERVER_EXEC='/robot/main.py'
#SERVER_EXEC='/robot/ds4move.py'

## TODO: Check if internet connection exists.
##       Add timer to skip updating code if takes to long
##       update code in other dir, once done, replace existing dir's code

## Get the latest code from git repo

## Run the robot program
python3 "${CURRENT_DIR}${SERVER_EXEC}"
