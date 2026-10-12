import os


def get_required_env_var(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable '{name}' is required.")
    return value


if __name__ == "__main__":
    print(get_required_env_var("sheety_user_name"))
    print(get_required_env_var("sheety_password"))
    print(get_required_env_var("sheety_url"))
