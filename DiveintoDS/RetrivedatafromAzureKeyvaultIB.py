#program to read  secret value from KeyVault using  interactive  Browser (IB)credetnials.

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
# read data from SQL Azure to DataFrame 
   # use defaulte credentials to connect to Azure , we are using basic Intaractive browser login method to enable DefaultAzureCredential() 
   # Read Azure SQL connection string from KeyVaulut 
   # Read data from Azure SQL Table to DataFrame 
   # print data from dataframe 
# Read Azure SQL connection string from KeyVaulut 
keyvaultUri = "https://gvsappconfigs.vault.azure.net"  #key vault URL, it is unique so , no need to specify container details 
credential = DefaultAzureCredential(exclude_interactive_browser_credential=False,additionally_allowed_tenants="*")   #opens a browser to capture token, additionally_allowed_tenants attribute enabels to scan through all allowed tenants
client = SecretClient(vault_url=keyvaultUri, credential=credential) #establish connection to keyvalut using credentials
secretname= "datastore"   #key vault secret name 
sqlConnectionString = client.get_secret(secretname)  # reading value from keyvault secret 
print(sqlConnectionString.value); 