#!/bin/bash
docker run -it --net=host --mount src="$(pwd)",target=/app,type=bind --rm aoc2019 python3 $1.py