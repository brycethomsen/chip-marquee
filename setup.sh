#!/bin/bash

cd $HOME
git clone git@github.com:brycethomsen/chip_marquee.git
CHIP_USER=$USER

sudo su -
cd /home/$CHIP_USER

# intial update (assuming you already have wifi configured)
apt-get update
apt-get install \
             python-pip \
             git
apt-get upgrade -y

# Pip packages
pip install pip --upgrade
pip install virtualenv

# setup virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements
