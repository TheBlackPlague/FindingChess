# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04 as Main

LABEL authors = "Shaheryar"

# Update the system and install necessary packages
RUN apt-get update && apt-get install -y \
    libqt5core5a \
    python3 \
    python3-pip \
    gcc \
    g++ \
    cmake \
    libtbb-dev \
    git \
    wget \
    lsb-release \
    software-properties-common \
    gnupg \
    tar \
    ninja-build

# Download and run the llvm.sh script to install Clang 16.0
RUN wget https://apt.llvm.org/llvm.sh && \
    chmod +x llvm.sh && \
    ./llvm.sh 16 && \
    rm -rf llvm.sh

# Create symbolic links to use clang-16 and clang++-16 as clang and clang++
RUN ln -s /usr/bin/clang-16 /usr/bin/clang && \
    ln -s /usr/bin/clang++-16 /usr/bin/clang++

# Download and Install Golang
RUN wget https://go.dev/dl/go1.20.4.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz && \
    rm -rf go1.20.4.linux-amd64.tar.gz

# Mark the Environment Variables CC and CXX to clang and clang++.
ENV CC clang
ENV CXX clang++
ENV PATH $PATH:/usr/local/go/bin

# Make sure the Python dependencies are met
RUN python3 -m pip install pip --upgrade &&  \
    python3 -m pip install requests

# Make sure we have the Client.py script
COPY ["DockerClient.py", "DockerClient.py"]

# Make sure we have the Shell Runner
COPY ["run.sh", "run.sh"]

ENTRYPOINT /bin/bash run.sh
