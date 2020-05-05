#!/bin/sh

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


set -e

until nc -vz ${KAFKA_SERVER_SERVER_NAME} ${KAFKA_SERVER_SERVER_PORT}; do
  >&2 echo "Waiting for Kafka to be ready... - sleeping"
  sleep 2
done

exec "$@"