Access container with:

    docker-compose run --rm web bash

Then make migrations.

    python manage.py makemigrations
    python manage.py migrate

Load fake data with following commands:

    python manage.py loaddata fixtures/vehicle_fake_data.json
    python manage.py loaddata fixtures/navigation_record_fake_data.json
    python manage.py loaddata fixtures/bin_fake_data.json
    python manage.py loaddata fixtures/operation_fake_data.json


Then, open new terminal session in project root folder and run

    Docker-compose run

