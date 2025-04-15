FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04
LABEL org.opencontainers.image.authors="jennyl.smith12@gmail.com"

# software versions for project dependencies 
ENV QUARTO_VER='1.7.13'
ENV QUARTO_ARCH='amd64'

# location for dependencies
ENV DIR='/opt'

# update packages and install dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential gfortran \
    zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
    libssl-dev libreadline-dev libffi-dev \
    wget xorg openbox gh

# install quarto
RUN wget -q -P $DIR https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VER}/quarto-${QUARTO_VER}-linux-${QUARTO_ARCH}.tar.gz && tar -xzf $DIR/quarto-${QUARTO_VER}-linux-${QUARTO_ARCH}.tar.gz -C $DIR
ENV PATH=$PATH:${DIR}/quarto-${QUARTO_VER}/bin
