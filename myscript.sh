#!/bin/bash
echo adduser
read username
echo add password
read password
echo what group
read group
useradd -p $password $username
usermod -aG $group $username

