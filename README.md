# Anti-no u
A bot that automatically responds to various different variations of "no u" with "no u."

## Usage
Here's the link to [add it to your server](https://discord.com/api/oauth2/authorize?client_id=697143422623940688&permissions=52288&scope=bot).

It doesn't require administrator permissions, so feel free to deny it view access to channels you don't want it to work in.
## Why not just use triggers from a bot like [Carl](https://carl.gg/)?
While triggers from Carl and others are great, they're too slow for this.

As you can see, there appears to be some kind of cooldown on the triggers, **so users can just say "no u" for a second time and defeat the entire system.** I'm assuming this is the case for most bot's custom triggers, if you find a bot that doesn't have this, feel free to use it instead.
![A gif showing Carl's triggers responding to "no u" messages](https://github.com/NaCl10/noubot/blob/master/readme-gifs/carl.gif)

However, because this bot's triggers are hardcoded, they will respond to *every* message.
![A gif showing this bot's triggers responding to "no u" messages](https://github.com/NaCl10/noubot/blob/master/readme-gifs/anti%20no%20u%20bot.gif)

## An important note
This bot is known to be ***extremely*** sensitive to "no u" and will *frequently* trigger false positives.

## Selfhosting
### Setup
#### Outside of Docker
Head over to the [releases](https://github.com/NaCl10/noubot/releases) and download the file main.py from the latest stable release.

Run main.py (Make sure you're in the same directory with main.py and that it's a directory where you're okay with main.py living semi-permanately):
```shell
python3 main.py
```
It will error out. This is because you need to enter a valid bot token in config.ini. See [configuration](https://github.com/NaCl10/noubot#configuration) for more information on that.

After configuration, run main.py again to actually start the bot. It's recommended to use some way of autostarting the script and to run it on a machine that will have high uptime, like a server.

#### With Docker
NOTE: The repository on Docker Hub is called "naclbot" rather than "noubot" because this project used to be called "naclbot," and the name was changed to "noubot," but Docker Hub is dumb and won't let you chance repository names.

Pull and run the container:
```shell
docker run -v /path/to/config.ini:/bot/config.ini --restart always -d --name noubot nacl10/naclbot
```
NOTES: You can specify a particular version of the bot by adding `:release-<version number here>` (DO NOT prefix the version number with "v") to the end of `nacl10/naclbot`. The path to config.ini shouldn't actually have a file called config.ini in it yet, it should just be where you want config.ini to be.  Make sure the path to config.ini ends in config.ini, even though config.ini doesn't exist yet. You can *technically* call the container something other than "noubot," but it's not recommended.

It will error out. This is because you need to enter a valid bot token in config.ini. See [configuration](https://github.com/NaCl10/noubot#configuration) for more information on that.

After configuration, start the container again:
```shell
docker start noubot
```
It's recommended to run the container on a machine that will have high uptime, like a server.

### Configuration
First, make sure you've run main.py (or the Docker container) at least once to generate the config file.

Then, edit the configuration file with your text editor of choice. Outside of Docker, it'll be wherever main.py is (provided you ran main.py from the directory that contains main.py). With Docker, it'll be wherever you put it.

Values:
| Value | Description | Required |
| ----- | ----------- | -------- |
| token | The bot token. Information about getting a bot token can be found in [the only good part of the discord.py documentation](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro). | Yes |
| status | Discord will display this as what the bot is "playing". It comes set to "no YOU!" by default, you can set it to whatever you want. | No |

### Updating
#### Outside of Docker
Delete main.py (DO NOT delete config.ini), download the new main.py from the [releases](https://github.com/NaCl10/noubot/releases), put it where the old main.py was, and run it again/restart your service. Simple as that.

#### With Docker
First, pull the new image:
```shell
docker pull nacl10/naclbot
```
Then, stop and remove the old container:
```shell
docker stop noubot && docker rm noubot
```
Finally, re-create the container with the new image:
```shell
docker run -v /path/to/config.ini:/bot/config.ini --restart always -d --name noubot nacl10/naclbot
```

## Contributing
Just open a pull request! That's what open source is all about. 

If you don't know how to code but you found a bug or have an issue, open an issue.
