#!/bin/sh

if [ $# -ne 1 ]
  then
    echo "Error: only one argument required"
    exit 1
fi

curl -sI --head $1 |grep -i Location|cut -d' ' -f2



