import yaml


def get_credentials_file():
    with open('../../resources/credentials.yml', 'r') as file:
        return yaml.safe_load(file)
