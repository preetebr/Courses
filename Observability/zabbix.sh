#!/bin/bash

# Atualização de sistema
sudo apt update
sudo apt upgrade -y

# Instalação de pacotes
sudo apt install -y wget gnupg2 lsb-release

# Add Zabbix repository
wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_7.0-1+ubuntu24.04_all.deb
sudo dpkg -i zabbix-release_7.0-1+ubuntu24.04_all.deb
sudo apt update

# Instalação do Zabbix server, frontend e agent
sudo apt install -y zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-agent

# Instalação MySQL server
sudo apt install -y mysql-server

# Configuração do MySQL para Zabbix
sudo mysql -e "CREATE DATABASE zabbix CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;"
sudo mysql -e "CREATE USER 'zabbix'@'localhost' IDENTIFIED BY 'zabbix_password';"
sudo mysql -e "GRANT ALL PRIVILEGES ON zabbix.* TO 'zabbix'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Importe o schema inicial de dados:
zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -pzabbix_password zabbix

# Configuração da conexão do zabbix 
sudo sed -i 's/# DBPassword=/DBPassword=zabbix_password/' /etc/zabbix/zabbix_server.conf

# Configurando PHP para o frontend
sudo sed -i 's/# php_value date.timezone Europe\/Riga/php_value date.timezone UTC/' /etc/zabbix/apache.conf

# Iniciando o zabbix server e o agent
sudo systemctl restart zabbix-server zabbix-agent apache2
sudo systemctl enable zabbix-server zabbix-agent apache2

# Informação de servidor instalado
echo "Zabbix installation completed."
echo "Open your browser and navigate to http://your_server_ip_or_domain/zabbix"
echo "Use 'Admin' as username and 'zabbix' as password to log in for the first time."
