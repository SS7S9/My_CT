# DAW.AA Supply Chain API

This repository is the API for the DAW.AA supply chain project. 

When installed using `pip3 install .` the command `daw_aa_api` will be added to your path.
You can then use the following commands

```bash
# Create a JWT to authenticate in the API
daw_aa_api jwt 

# Start the API program
daw_aa_api start 
```

Additionally you can specify a config file with the config switch
```bash
daw_aa_api -c <config_file>
# Or
daw_aa_api --config <config_file>
```

For more detail, use the help command
```bash
daw_aa_api --help
```

If you want to run this project directly without installing you can also use the `api.py` file
```bash
python3 api.py --help
```

Config file should follow the following format
```yaml
# DB Connection URI
db: sqlite+aiosqlite:// # In-memory SQLite database URI

# API JWT Key
jwt_key: SOME_RANDOM_STRING # Make sure you set this to something appropriately random  

# API Options
api:
  host: 0.0.0.0
  port: 8000

# Optional CORS settings
# This is not needed when using the reverse proxy
cors: 
  allow_origins:
    - http://localhost:3000
  allow_methods:
    - "*"
  allow_headers:
    - "*"
  allow_credentials: true

# Manually override invalid redirect
redirects:
  invalid_uid: /invalid
```

In order to host the single page static files, you need to build the daw.aa.supply_chain_dash also

## Running tests

If you'd like to run some of the test cases, first ensure you've opened the devcontainer enviroment 
(Open the dir contiaining .devcontainer in vscode, then use "Reopen in Container" - see https://code.visualstudio.com/docs/devcontainers/containers)

Switch to the tests folder and try some of the following:

```bash
pytest api/client.py
pytest api/validations.py
# ... and so on
```