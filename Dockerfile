FROM continuumio/anaconda3
RUN conda update --all && \
    conda install -c conda-forge graph-tool && \
    mkdir /app

WORKDIR /app

# docker build . -t aoc2016 --network host
# docker run -it --net=host --mount src="$(pwd)",target=/app,type=bind --rm aoc2016/6 /bin/bash