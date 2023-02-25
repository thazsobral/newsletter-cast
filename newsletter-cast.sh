#!/bin/bash
python3 ./collector-bot/collector-bot.py &&
python3 ./converter-bot/converter-bot.py &&
python3 ./publisher-bot/publisher-bot.py

rm ./common/scripts-txt/*.txt &&
rm ./common/files-audio/*.mp3