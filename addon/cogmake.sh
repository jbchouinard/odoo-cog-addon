#!/usr/bin/env bash
python -m cogapp -d -o cogfiles.txt cogfiles.cog.txt
python -m cogapp -I . @cogfiles.txt
