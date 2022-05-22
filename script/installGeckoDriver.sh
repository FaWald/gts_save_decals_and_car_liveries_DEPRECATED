#!/bin/bash

sudo apt-get update
sudo apt-get upgrade

wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -zxvf geckodriver-v0.30.0-linux64.tar.gz

sudo mv geckodriver /usr/bin/geckodriver
sudo chown root:root /usr/bin/geckodriver
sudo chmod +x /usr/bin/geckodriver
