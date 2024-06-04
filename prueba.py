import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Obtener variables de entorno
key_vault_name = os.environ["keys2Leo"]
secret_name = os.environ["secreto"]

# Crear URL del Key Vault
KVUri = f"https://{key_vault_name}.vault.azure.net"

# Autenticar usando DefaultAzureCredential
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

# Obtener el secreto
retrieved_secret = client.get_secret(secret_name)

# Imprimir el secreto
print(f"Your secret value is: {retrieved_secret.value}")
