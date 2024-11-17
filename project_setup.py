import subprocess
import json


def check_git_installed():
    """Check if Git is installed."""
    try:
        subprocess.run(
            ["git", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_input(prompt, default=None):
    """Get input from user with an optional default value."""
    if default:
        prompt += f" [default = {default}] "
    prompt += ": "
    user_input = input(prompt).strip()
    return user_input if user_input else default


def get_current_envs() -> dict[str, str | None]:
    try:
        with open(".env", "r") as f:
            lines = f.readlines()
            print(lines)
            return {
                b[0]: b[1]
                for a in lines
                if (c := a.strip()) and len(b := c.split("=", maxsplit=1))
            }
    except Exception:
        return {}


def get_json_from_file(filename: str) -> dict[str, str]:
    try:
        with open(filename, "r") as f:
            return dict(json.load(f))
    except Exception:
        return {}


required_envs: dict[str, list[str | None]] = {
    "DISCORD_TOKEN": [
        "Enter Discord Token",
        None,
    ],
    "NOTION_SECRET": [
        "Enter NOTION API Key",
        None,
    ],
    "NOTION_DATABASE_ID": ["Enter NOTION target database ID", None],
}


def main():
    print("Welcome to the ICRS Lab Project Setup CLI!")

    GIT_INIT = get_input("Run git submodule init: [Y/N]", "Y").upper() == "Y"
    if GIT_INIT:
        if not check_git_installed():
            print("Git not installed, please install git and try the script again!")
            exit(1)
        subprocess.run(
            ["git", "submodule", "update", "--recursive", "--remote", "--init"]
        )
        subprocess.run(["bash", "update.sh"])

    current_envs = get_current_envs()
    print(current_envs)
    update_env_keys = required_envs.keys() - current_envs.keys()
    if not update_env_keys:
        print("All env variables are up to date!")

    else:
        for k in required_envs.keys() - current_envs.keys():
            v = required_envs[k]
            var = get_input(v[0], v[1])
            if v[1] is None and var is None:
                print(f"No {k} Provided!")
                exit(1)
            current_envs[k] = var

    print("\n============================================================")
    print("Setting Up Discord files")
    print("============================================================\n")

    def set_discord_settings(exisiting_settings):
        DISCORD_GUILD_ID = get_input("Discord Guild Id")
        if not DISCORD_GUILD_ID:
            print("No Discord GUILD ID Provided!")
            exit(1)

        ADMIN_ID = get_input("Discord Admin Id")
        if not ADMIN_ID:
            print("No Discord ADMIN ID Provided!")
            exit(1)

        PREFIX = "!"
        discord_settings_json = {
            "PREFIX": PREFIX,
            "DISCORD_GUILD_ID": DISCORD_GUILD_ID,
            "ADMIN_ID": ADMIN_ID,
        }
        print("Creating Discord Settings json")
        with open("discord_settings.json", "w") as f:
            json.dump(discord_settings_json, f)

        print("Finished Discord Settings json\n")

    discord_settings = set(["PREFIX", "DISCORD_GUILD_ID", "ADMIN_ID"])
    existing_discord_settings = get_json_from_file("discord_settings.json")
    if existing_discord_settings and len(
        discord_settings - existing_discord_settings.keys()
    ) != len(discord_settings):
        msg = (
            f"Discord Settings Found\n{existing_discord_settings}\n"
            "Do you want to overwrite: [Y/N]"
        )
        if get_input(msg, "N").upper() == "Y":
            set_discord_settings(exisiting_settings=existing_discord_settings)
    else:
        set_discord_settings(exisiting_settings=existing_discord_settings)

    print("\n============================================================")
    print("Setting Up RabbitMQ Config File")
    print("============================================================\n")

    # RabbitMQ Settings
    EXCHANGE_NAME = get_input("Enter RabbitMQ Exchange name", "printer")

    # Printer Settings config
    PRINTER_NAMES = ["test1"]
    PRINTER_GATEWAY_ENDPOINT_SUFFIX = "-printer-gateway-endpoint/"
    rabbitmq_json = {"EXCHANGE_NAME": EXCHANGE_NAME}

    with open("rabbitmq.json", "w") as f:
        json.dump(rabbitmq_json, f)

    print("Finished RabbitMQ Settings json\n")
    print("============================================================")
    MEME_DB = "postgres"
    if update_env_keys:
        print("Creating env file")
        with open(".env", "w") as f:
            f.write(f"MEME_DB={MEME_DB}\n")
            for k, v in current_envs.items():
                f.write(f"{k}={v}\n")

        print("Finished env file\n")
        print("============================================================")

    print("Creating printer settings json")
    printer_settings_json = {
        "PRINTER_NAMES": PRINTER_NAMES,
        "PRINTER_GATEWAY_ENDPOINT_SUFFIX": PRINTER_GATEWAY_ENDPOINT_SUFFIX,
    }
    with open("printer_settings.json", "w") as f:
        json.dump(printer_settings_json, f)

    print("Finished printer settings json\n")
    print("============================================================")


if __name__ == "__main__":
    main()
