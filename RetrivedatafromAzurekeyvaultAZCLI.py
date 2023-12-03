#program to read  secret value from KeyVault using Azure CLi session.
#Isntall Azure CLI in your dev machine from https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli#install-or-update,after installing, close your python editor and reopen , it enabel python to read CLI path
#befor running the program change the terminal to powershell and run command AZ login
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
# read data from SQL Azure to DataFrame 
   # use defaulte credentials to connect to Azure , we are using basic Intaractive browser login method to enable DefaultAzureCredential() 
   # Read Azure SQL connection string from KeyVaulut 
   # Read data from Azure SQL Table to DataFrame 
   # print data from dataframe 
# Read Azure SQL connection string from KeyVaulut 
keyvaultUri = "https://gvsappconfigs.vault.azure.net"  #key vault URL, it is unique so , no need to specify container details 
credential = DefaultAzureCredential( )   #it uses the token generated from  AZ login command exection in the terminal before executing this program
client = SecretClient(vault_url=keyvaultUri, credential=credential) #establish connection to keyvalut using credentials
secretname= "datastore"   #key vault secret name 
sqlConnectionString = client.get_secret(secretname)  # reading value from keyvault secret 
print(sqlConnectionString.value); 