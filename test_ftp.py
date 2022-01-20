from ftplib import *

ftp=FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

#creating username and password
user=input("Enter the user: ")
password= input("Enter the password: ")

#passing username and password as parameters
ftp.login(user, password)

#showing what directory it is in now
print("Current work directory: ", ftp.pwd())

#changing the directory
ftp.cwd('pub')

print("Current directory: ", ftp.pwd())

#listing all files present in that folder
print(ftp.retrlines('LIST'))

ftp.quit()