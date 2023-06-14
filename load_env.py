def read_env(file_path):
    """Read the .env file keys."""
    env = {}

    for line in open(file_path, "r"):
        key_value = line.split("=")
        env[key_value[0].strip()] = key_value[1].strip()

    return env


# print(read_env(".env"))
