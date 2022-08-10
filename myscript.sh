#!/bin/bash

# Don't forget to comment
echo adduser
read username
echo add password
read password
echo what group
read group

sudo useradd -p $password $username
sudo addgroup $group
sudo usermod -aG $group $username
