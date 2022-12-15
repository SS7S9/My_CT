import yaml
from pathlib import Path
import jsonschema

config = {}

config_schema = {
    "type": "object",
    "properties": {
        "db": {
            "type": "string",
            "description": "Database connection URI"
        },
        "jwt_key": {
            "type": "string",
            "description": "Secure key for generating and verifying JWT"
        },
        "api": {
            "type": "object",
            "description": "Options for API",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "API bind port"
                },
                "port": {
                    "type": "integer",
                }
            },
        },
        "static": {
            "type": "string"
        },
        "redirects": {
            "type": "object",
            "properties": {
                "invalid_uid": {
                    "type": "string"
                },
            },
            "required": ["invalid_uid"]
        },
        "trusted_proxies": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "cors": {
            "type": "object",
            "properties": {
                "allow_origins": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "allow_methods": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "allow_headers": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "allow_credentials": {
                    "type": "boolean"
                },
            },
        }
    },
    "required": ["db", "jwt_key", "redirects"]
}


def load_config(config_path: Path):
    new_config = yaml.safe_load(config_path.read_text())
    set_config(new_config)


def set_config(new_config: dict):
    jsonschema.Draft7Validator(schema=config_schema).validate(
        instance=new_config)

    config.clear()
    config.update(new_config)