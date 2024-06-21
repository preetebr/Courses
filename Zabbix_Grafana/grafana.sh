#Instalação dos Pré-requisitos:
sudo apt-get install -y apt-transport-https software-properties-common wget 

#Importe as chaves GPG: 
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null

#Instalação Grafana
sudo apt-get install -y adduser libfontconfig1 musl
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_11.0.0_amd64.deb 
sudo dpkg -i grafana-enterprise_11.0.0_amd64.deb 

#Inicie os serviços do Grafana: 
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server

#Validação dos serviços em execução: 
sudo systemctl status grafana-server

#Configuração para o Grafana iniciar junto ao SO usando o systemd:
sudo systemctl enable grafana-server.service

#Liberação de porta < 1024
sudo systemctl edit grafana-server.service

#Reiniciei o Grafana usando systemd:
sudo systemctl restart grafana-server
