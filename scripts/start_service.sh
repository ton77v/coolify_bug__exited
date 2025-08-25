#!/bin/bash
# scripts/start_service.sh
# start dev | staging | production environment service @ docker-compose stack

# ...


# (3) and starting the server
echo "🚀 STARTING THE SERVER..."
# cd src || exit 1  # we should be in /root => /root/src
# we need to preserve the same path to the `APP_CONFIG_PATH`
# so we'll add to PYTHONPATH instead of changing PWD
PYTHONPATH="$(pwd)/src:${PYTHONPATH}"
export PYTHONPATH
. start_server.sh
