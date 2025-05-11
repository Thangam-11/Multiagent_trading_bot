import os
import yaml

def load_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, '..', 'config', 'config.yaml')
    config_path = os.path.abspath(config_path)

    with open(config_path, "r") as file:
        return yaml.safe_load(file)
