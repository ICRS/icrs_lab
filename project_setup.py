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
        prompt += f" [{default}]: "
    user_input = input(prompt).strip()
    return user_input if user_input else default


def main():
    print("Welcome to the ICRS Lab Project Setup CLI!")

    GIT_INIT = get_input("Run git init: [Y/N]", "Y").upper() == "Y"
    if GIT_INIT:
        if not check_git_installed():
            print("Git not installed, please install git and try the script again!")
            exit(1)
        subprocess.run(
            ["git", "submodule", "update", "--recursive", "--remote", "--init"]
        )

    DISCORD_TOKEN = get_input("Enter Discord Token")
    if not DISCORD_TOKEN:
        print("No Discord Token Provided!")
        exit(1)

    DISCORD_GUILD_ID = get_input("Discord Guild Id")
    if not DISCORD_GUILD_ID:
        print("No Discord GUILD ID Provided!")
        exit(1)

    ADMIN_ID = get_input("Discord Admin Id")
    if not ADMIN_ID:
        print("No Discord ADMIN ID Provided!")
        exit(1)

    MEME_DB = "postgres"

    # RabbitMQ Settings
    EXCHANGE_NAME = get_input("Enter RabbitMQ Exchange name", "printer")

    # Printer Settings config
    PRINTER_NAMES = ["test1"]
    PRINTER_GATEWAY_ENDPOINT_SUFFIX = "-printer-gateway-endpoint/"

    print("============================================================")
    print("Generating files")
    print("============================================================")
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

    print("============================================================")

    rabbitmq_json = {"EXCHANGE_NAME": EXCHANGE_NAME}

    print("Creating RabbitMQ json file")

    with open("rabbitmq.json", "w") as f:
        json.dump(rabbitmq_json, f)

    print("Finished RabbitMQ Settings json\n")
    print("============================================================")

    print("Creating env file")
    with open(".env", "w") as f:
        f.write(f"DISCORD_TOKEN={DISCORD_TOKEN}")
        f.write(f"MEME_DB={MEME_DB}")

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
