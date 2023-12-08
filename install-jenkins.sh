#!/bin/bash

# Ensure keyrings directory exists
sudo mkdir -p /etc/apt/keyrings/

# Add Eclipse Adoptium repository
sudo wget -O /etc/apt/keyrings/adoptium.asc \
  https://packages.adoptium.net/artifactory/api/gpg/key/public
echo "deb [signed-by=/etc/apt/keyrings/adoptium.asc] \
https://packages.adoptium.net/artifactory/deb \
$(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" \
  | sudo tee /etc/apt/sources.list.d/adoptium.list > /dev/null

# Add Jenkins LTS repository
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update
# Java needs to be installed before attempting to install Jenkins,
# otherwise "Errors [are] encountered while processing jenkins"
sudo apt-get install --assume-yes temurin-17-jdk
sudo apt-get install --assume-yes jenkins

# This can just be done through a normal cloud-config, it's in the Ubuntu universe
sudo apt-get install -y podman

# Allow rootless Podman
sudo usermod --add-subuids 165536-231071 --add-subgids 165536-231071 jenkins
sudo loginctl enable-linger $(id -u jenkins)
sudo -u jenkins podman system migrate
