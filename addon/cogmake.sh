#!/usr/bin/env sh
python -m cogapp -d -o cogfiles.txt cogfiles.cog
python -m cogapp -I . @cogfiles.txt
