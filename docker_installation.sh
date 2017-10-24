#!/usr/bin/env bash
# Script with all the instrunctions from Docker Community Installation Guide from their official Website.
# This script uses the apt manager to install the stable releases by adding the official PPA repository.

echo "Removing previous Versions of docker or docker-engine. It's okay"
echo "if none of these packages were previously not installed"
sudo apt-get remove docker docker-engine docker.io
echo "Most users set up Docker’s repositories and install from them, for ease of installation and upgrade tasks. This is the recommended approach."
echo "Updating the apt package index"
sudo apt-get update
echo "Installing Packages to allow apt to use a repository over HTTPS"
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
echo "Adding Docker's official GPG Key"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
echo "Verifying the fingerprint"
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
echo "Setting up the Respository is Now complete."
sudo apt-get update
sudo apt-get install docker-ce
echo "Verifying Docker CE Installation"
sudo docker run hello-world