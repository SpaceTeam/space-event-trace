# space-event-trace

Tracing service for [TU Wien Spaceteam](https://spaceteam.at/?lang=en) events.
![Screenshot](https://user-images.githubusercontent.com/21206831/147995219-c73f22a5-0e8d-4809-b209-09e9d38e4219.png)

This service is a special adaption of 
[Space Trace](https://github.com/SpaceTeam/space-trace).

## Getting started

Install Python3.8 (or higher), zbar, popper, libxml2

Install all dependencies with:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=space_trace FLASK_ENV=development
flask run
```

This launces a simple webserver which can only be accessed from the localhost.

**Note:** Don't use this server in production, it is insecure and low
performance.

## Deployment

How we deploy this app on Ubuntu.

Install the requirements with:

```bash
sudo apt -y install python3-venv python3-pip libzbar0 libxml2-dev libxmlsec1-dev libxmlsec1-openssl poppler-utils
```

Create a virtual env with:

```bash
python3 -m venv venv
```

You maybe want to copy over the vaccine status of all users from 
[space trace](https://github.com/SpaceTeam/space-trace). In that case you can
just copy the sqlite file from spacetrace and run the script in 
`scripts/migrate_db.sql`.

Copy `instance/config_example.toml` to `instance/config.toml` and edit all
the fields in it.

The seats in the database need to be created manually. To create them run
`FLASK_APP=space_trace FLASK_ENV=development flask create-db`.

Open `space-event-trace.service` and edit the username and all paths to the working
directory.

Start the systemd service with:

```bash
sudo cp space-event-trace.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable space-event-trace.service
sudo systemctl start space-event-trace.service
```

The service should now be up and running 🎉

To stop the service run:

```bash
sudo systemctl stop space-event-trace.service
```

To update the service to a new version (commit) run:

```bash
git pull
sudo systemctl restart space-event-trace.service
```

## Development

- Use [`black`](https://github.com/psf/black) to format code
- Try to follow the python style guide [PEP 8](https://www.python.org/dev/peps/pep-0008/)