#!/usr/bin/env bash
# Install system dependencies for numpy and other libraries
apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran \
    liblapack-dev \
    libblas-dev \
    python3-dev
