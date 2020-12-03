#!/bin/bash

# I'm aware how bad practice this *seems*, but discord.py is shit and won't run AT ALL unless it's the latest version and I don't feel like rebuilding my image EVERY SINGLE TIME discord.py updates.
python3 -m pip install -U discord.py

cd /bot
python3 /bot/main.py
