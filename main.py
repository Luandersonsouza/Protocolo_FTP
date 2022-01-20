#script que irá rodar o protocolo FTP!
from ftplib import *

ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())

ftp.quit()
