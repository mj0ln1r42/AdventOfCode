# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.241.1/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-buster"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ARG USER="vscode"
ARG USER_HOME="/home/${USER}"

# Install any other tools we need
RUN apt-get update \
    && ACCEPT_EULA=Y apt-get install --no-install-recommends -y dos2unix

# Install our python dependencies from requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

# Copy user-sepcific .bash_aliases and make it linux friendly
COPY .devcontainer/.bash_aliases ${USER_HOME}/.bash_aliases
RUN dos2unix ${USER_HOME}/.bash_aliases \
    && apt-get --purge remove -y dos2unix
