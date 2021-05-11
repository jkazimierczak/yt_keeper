import sys

import pkg_resources
import yaml
from pathlib import Path
from pydantic import BaseModel, HttpUrl, ValidationError, conlist, validator

from . import RELATIVE_ROOT


class ConfigModel(BaseModel):
    output_to: str
    output_template: str
    playlists: conlist(HttpUrl, min_items=1)

    @validator('output_to')
    def resolve_path(cls, v):
        if not Path(v).is_absolute():
            v = RELATIVE_ROOT / v
        return Path(v).resolve()

    class Config:
        allow_mutation = False


def load() -> ConfigModel:
    """Load configuration from file."""
    config_file = Path.home() / '.config' / 'yt_keeper' / 'config.yml'
    if not config_file.exists():
        raise FileNotFoundError('Config not found in desired location.')

    with open(config_file) as f:
        try:
            config = yaml.safe_load(f)
            if not config.get('playlists'):
                print('Add playlists you want to keep to the config and try again.')
                print(f'Config location: {config_file}')
                sys.exit(1)
            return ConfigModel(**config)
        except ValidationError as e:
            print(e)
            sys.exit(1)
