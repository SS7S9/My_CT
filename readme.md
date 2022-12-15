# DAW.AA Supply Chain Services

This repository contains the stack for the collection of data (and hosting of the landing page) for the DAW.AA Supply Chain project.

The docker-compose.yml file defines the structure for the service stack, which consists of:

- Dash
    - The dash is a webapplication built in React.js, and statically hosted by the nginx reverse proxy
- API
    - The API is a Python application using the FastAPI and sqlalchemy libraries
    - It was previously a package hosted by the sense-t pypi package server, but now updated to run locally
- Nginx
    - The nginx service acts as a reverse proxy for the API, providing SSL termination
    - It also hosts the static dash files (Copied into a volume on stack up from the built image)

For accessing the MySQL database in dev and production, I usually use MySQL Workbench. Likewise, I tend to dev in WSL2 (windows), but
windows (native), mac or linux dev environments should also work.

## Deployment 

In general to get started you need:
- API config file (config.yml)
- Docker overrides (docker-compose.override.yml)

The format for `config.yml` is specified under `daw.aa.supply_chain_api/README.md`

Basic `config.yml`:
```yaml
db: mysql+aiomysql://root:MYSQL_PASSWORD@mysqldb:3306/daw_aa_supply_chain_api
jwt_key: SOME_RANDOM_STRING # use something like: "openssl rand -base64 32" to generate this
api:
  host: 0.0.0.0
  port: 8000
redirects:
  invalid_uid: /invalid
```

Basic `docker-compose.override.yml`:
```yaml
version: "3"

services:
  mysqldb:
    environment:
      MYSQL_ROOT_PASSWORD: MYSQL_PASSWORD
```

Be sure to substitute `MYSQL_PASSWORD` with an actual password!

If you're unfamilliar with docker, or specifically docker-compose, it may be benificial to read up on them.

Once configured, the system can be built and deployed. 
If any changes are made to the repos, the changes can be pulled, rebuilt and redeployed.

Useful docker-compose commands:

```bash
# Build images (Will need if you make changes), be sure to run up after a build to refesh running services
docker-compose build

# Start stack with logs detached
docker-compose up -d

# View stack logs, tail shows log end
docker-compose logs --tail 100

# View logs for a specific service (api in this case)
docker-compose logs --tail 100 api

# Shut down stack
docker-compose down

# View currently running services
docker-compose ps

# You can also view all docker container stats with
docker stats
```

## Development

Both the API and the frontend can be developed in devcontainers (https://code.visualstudio.com/docs/devcontainers/containers)

These run locally and allow you to develop within a tighter development loop cycle. 

For example: If you were developing the frontend, you could open the frontend devcontainer, specify your backend (either hosted locally as well, or some other hosting location) in a .env file and begin hotloaded dev with `yarn start`.

An example `.env` file for dev
```env
REACT_APP_API_URL=http://localhost:8000
```
Using the `REACT_APP_API_URL` environmental variable in this way, you can point the locally running frontend to a different backend for dev.

For the backend development, once the devcontainer is running you can use testcases (or an external program such as postman) to simulate requests from the frontend.

Alternatively, the entire stack can also be hosted locally though the same method as deployment (Specify `config.yml` and `docker-compose.override.yml`, and use docker-compose to build and run)

Example `docker-compose.override.yml` for dev:
```yaml
version: "3"

services:
  reverse_proxy:
    volumes:
      - "./ngix/local_dev.conf:/etc/nginx/conf.d/default.conf"
  mysqldb:
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
```

Example `config.yml` for dev:
```yaml
db: mysql+aiomysql://root:rootpass@mysqldb:3306/daw_aa_supply_chain_api
jwt_key: RANDOM_STRING # use something like: "openssl rand -base64 32" to generate this
api:
  host: 0.0.0.0
  port: 8000
redirects:
  invalid_uid: /invalid
```
