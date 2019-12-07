#!/bin/bash
docker run -it --net=host --mount src="$(pwd)",target=/app,type=bind --rm aoc2019 /bin/bash