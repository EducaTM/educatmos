#!/bin/bash

sudo apt update
sudo apt install -y git ansible

sudo ansible-pull -U https://github.com/EducaTM/educatmos.git -C master