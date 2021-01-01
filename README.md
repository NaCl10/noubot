# NaClbot
This is my bad Discord bot. People mainly use it because it automatically says "no u" back when someone says "no u".

## Usage
### Outside of Docker
Head over to the [releases](https://github.com/NaCl10/naclbot/releases) and download the file main.py from the latest stable release.

Run main.py (Make sure you're in the same directory with main.py and that it's a directory where you're okay with main.py living semi-permanately):
```shell
python3 main.py
```
It will error out. This is because you need to enter a valid bot token in config.ini. See [configuration](https://github.com/NaCl10/naclbot#configuration) for more information on that.

After configuration, run main.py again to actually start the bot. It's recommended to use some way of autostarting the script and to run it on a machine that will have high uptime, like a server.

### With Docker

Pull and run the container:
```shell
docker run -v /path/to/config.ini:/bot/config.ini --restart always -d --name naclbot nacl10/naclbot
```
NOTES: You can specify a particular version of the bot by adding `:release-<version number here>` (DO NOT prefix the version number with "v") to the end of `nacl10/naclbot`. The path to config.ini shouldn't actually have a file called config.ini in it yet, it should just be where you want config.ini to be.  Make sure the path to config.ini ends in config.ini, even though config.ini doesn't exist yet. You can *technically* call the container something other than "naclbot", but it's not recommended.

It will error out. This is because you need to enter a valid bot token in config.ini. See [configuration](https://github.com/NaCl10/naclbot#configuration) for more information on that.

After configuration, start the container again:
```shell
docker start naclbot
```
It's recommended to run the container on a machine that will have high uptime, like a server.

### Configuration

First, make sure you've run main.py (or the Docker container) at least once to generate the config file.

Then, edit the configuration file with your text editor of choice. Outside of Docker, it'll be wherever main.py is (provided you ran main.py from the directory that contains main.py). With Docker, it'll be wherever you put it.

Values:
| Value | Description | Required |
| ----- | ----------- | -------- |
| token | The bot token. Information about getting a bot token can be found in [the only good part of the discord.py documentation](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro). | Yes |
| status | Discord will display this as what the bot is "playing". It comes set to "echo 'R'; while true; do echo 'E'; done" by default, you can set it to whatever you want. | No |

## Updating
### Outside of Docker
Delete main.py (DO NOT delete config.ini), download the new main.py from the [releases](https://github.com/NaCl10/naclbot/releases), put it where the old main.py was, and run it again/restart your service. Simple as that.

### With Docker
First, pull the new image:
```shell
docker pull nacl10/naclbot
```
Then, stop and remove the old container:
```shell
docker stop naclbot && docker rm naclbot
```
Finally, re-create the container with the new image:
```shell
docker run -v /path/to/config.ini:/bot/config.ini --restart always -d --name naclbot nacl10/naclbot
```

## Contributing
Just open a pull request! That's what open source is all about. 

If you don't know how to code but you found a bug or have an issue, open an issue.
