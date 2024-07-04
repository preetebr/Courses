from pyVim.connect import SmartConnect, Disconnect
import ssl

# Configurações do vCenter
vcenter_server = 'vcenter.example.com'
username = 'myUsername'
password = 'myPassword'

# Ignorar certificados SSL não confiáveis
context = ssl._create_unverified_context()

# Conectar ao vCenter
si = SmartConnect(host=vcenter_server, user=username, pwd=password, sslContext=context)

# Verificar a conexão
if not si:
    raise Exception("Could not connect to the specified host using specified username and password")

# Desconectar do vCenter
#Disconnect(si)
#print("Conectado ao vCenter com sucesso e desconectado.")
