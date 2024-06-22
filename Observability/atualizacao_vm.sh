#!/bin/bash

# Atualização de lista de pacotes
sudo apt update

# Upgrade de lista de pacotes
sudo apt upgrade -y

# Upgrade da distro, caso necessário
sudo apt dist-upgrade -y

# Remove pacotes obsoletos
sudo apt autoremove -y

# Limpa pacotes e repositórios que não estão em uso
sudo apt clean

# Limpa o repositório local de arquivos
sudo apt autoclean

# Atualiza os pacotes snap
sudo snap refresh