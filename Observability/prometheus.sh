#Script para instalação do Prometheus

#Instalação e atualização de pacotes
sudo su - 
apt-get update
dnf -y install zlib-devel pam-devel openssl-devel libtool
bison flex autoconf gcc make git net-tools lsof net-tools

#criação de usuário prometheus
useradd -m -s /bin/false prometheus

#Repositório
cat prometheus_repo /etc/yum.repos.d/prometheus-rpm_release.repo


#Instalação
dnf install prometheus

#Validação
prometheus --version

#Criação de serviço 
cat service_repo /etc/systemd/system/prometheus.service

systemctl daemon-reload

#Start prometheus
systemctl start prometheus


#Instalação Node_exporter
dnf install node_exporter

#start e restart do node
systemctl start node_exporter
systemctl status node_exporter

#copiando informações do Node para o Prometheus
#Necessário alterar o IP no arquivo node_repo

cat nodeexporter_repo >> /etc/prometheus/prometheus.yml

#Validando as configurações
promtool check config /etc/prometheus/prometheus.yml

#restart na aplicação
systemctl restart prometheus





