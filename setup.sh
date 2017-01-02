#!/bin/bash

sudo su -
cd $HOME

# intial update
apt-get update
apt-get install \
             python-pip \
             git
apt-get upgrade -y

# Pip packages
pip install pip --upgrade
pip install virtualenv
