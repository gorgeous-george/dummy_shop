#!/usr/bin/env sh

set -o errexit
set -o nounset

cmd="$*"

postgres_ready () {
  # Check that postgres is up:
  sh '/wait-for-command.sh' -t 5 -s 0 52 -c "curl db_storage:5432"
}

# We need this line to make sure that this container is started
# after the one with postgres:
until postgres_ready; do
  >&2 echo 'Postgres is unavailable - sleeping'
done

# It is also possible to wait for other services as well: redis, elastic, mongo
>&2 echo 'Postgres is up - continuing...'

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd