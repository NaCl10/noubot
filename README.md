# NaClbot

This is my bad Discord bot. It doesn't do much, I mostly just made it to learn about making Discord bots and because I could.

## Usage

Head over to the [releases](https://github.com/NaCl10/naclbot/releases) and download the file `main.py` from the latest stable release.

Run main.py (IN THE SAME DIRECTORY AS THE FILE):

```shell
python3 main.py
```
It will error out. This is because you need to enter a valid bot token in config.ini.

Edit config.ini (which the script just generated) to contain your bot token. More info about getting a bot token can be found on [the only good part of the discord.py documentation](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro).

Then run main.py again to actually start the bot this time. It is reccomended to use some way of autostarting the bot script (and also to run it on a machine that will have high uptime, like a server).
