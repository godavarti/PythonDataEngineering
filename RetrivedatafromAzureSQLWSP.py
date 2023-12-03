#program to read data from Azure SQL.
import pyodbc  # we are using odbc driver to read the data from Azure SQL Server 
import pandas as pd #we are usign dataframe defined in pandas library to capature the ourput from SQL Azure 
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.identity import ClientSecretCredential
# read data from SQL Azure to DataFrame 
    #create database in Azure , enable SQL Authentication and the create user with SQL Autthentication  by connecting to SQL Azure Database 
        # Master Database 
         # CREATE LOGIN <logingname> WITH PASSWORD = <logingpassord>
         # CREATE USER <user name> FROM LOGIN <logingname>
         #User database 
         #  CREATE USER <user name>  FROM LOGIN logingname;
         #  ALTER ROLE db_datareader ADD MEMBER <user name>;
   #install ODBC driver in developper machince  Download ODBC Driver for SQL Server https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16
   # Create secret in KeyVault wiht name "datastore"
     # add secret value (SQL connection String) as below ,dont any trailing spaces or # in the begining 
     #  Driver=ODBC Driver 18 for SQL Server;Server=tcp:<sarvername>.database.windows.net,1433;Database=<user databasename>;UID=<SQL login Name>;PWD=<SQL Login Password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30
   # Program Sequence 
   # 1.Read Azure SQL connection string from KeyVaulut 
   # 2.frame connection wiht SQL Azure using pyodbc.connect() method
   # 3.design your SQL query 
   # 4.establish connection by executing  connectioncontext.cursor()
   # 5.Read data from Azure SQL Table to DataFrame using pd.read_sql()
   # print data from dataframe 
# Read Azure SQL connection string from KeyVaulut 
keyvaultUri = "https://gvsappconfigs.vault.azure.net"  #key vault URL, it is unique so , no need to specify container details 
credential = DefaultAzureCredential(exclude_interactive_browser_credential=False,additionally_allowed_tenants="*")   #opens a browser to capture token, additionally_allowed_tenants attribute enabels to scan through all allowed tenants, this credenitals used only to read azure keyvault
client = SecretClient(vault_url=keyvaultUri, credential=credential) #establish connection to keyvalut using credentials
secretname= "datastore"   #key vault secret name 
sqlConnectionString = client.get_secret(secretname).value  # reading value from keyvault secret 
Sqluser = "Gvspython"
Sqluserpword =client.get_secret(Sqluser).value
#sqlteant= client.get_secret('sqlteanantid').value
#sqlcredential =ClientSecretCredential(sqlteant,Sqluser,Sqluserpword)
sqlConnectionString="Driver=ODBC Driver 18 for SQL Server;Server=tcp:pytestgvs.database.windows.net,1433;Database=pytestgvs;UID="+Sqluser+ ";PWD="+Sqluserpword+ ";Authentication=ActiveDirectoryPassword;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
#print(sqlConnectionString)
# create connection context 
connectioncontext  = pyodbc.connect(sqlConnectionString)
cursor = connectioncontext.cursor()
# select to 10 rows from SQL table to insert in dataframe.
cursor.execute('''insert into employee values('gvs7',7,200000);''')
connectioncontext.commit();
sqlAzurequery = "select * From employee;"
df = pd.read_sql(sqlAzurequery, connectioncontext)
print(df.head(6))
connectioncontext.close() # close SQL connection 

