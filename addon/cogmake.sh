#!/usr/bin/env sh
python -m cogapp -d -o cogfiles.txt cogfiles.cog.txt
python -m cogapp -I . @cogfiles.txt
