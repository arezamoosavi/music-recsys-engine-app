#!/bin/sh
#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"