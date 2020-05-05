#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

echo "Migration started"

# python web.py db init
# python web.py db migrate
# python web.py db upgrade

# flask db init
# flask db migrate
# flask db upgrade

echo "Migration was Successfull"
sleep 1

# run gunicorn
gunicorn -w 1 web:flask_app -b 0.0.0.0:5000 --access-logfile '-' --workers ${GUNICORN_WORKERS} --timeout ${GUNICORN_TIMEOUT} $*
# gunicorn -w 1 web:flask_app -b :5000 --access-logfile '-'