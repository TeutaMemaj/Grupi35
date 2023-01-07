import os
import ftpConnection

# Credentials of the public FTP Server
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu" 

folder_path = 'C:\\Users\\HP\\Desktop\\Files'

def upload_files(ftp, local_folder):
    files = os.listdir(local_folder)
    for file in files:
        if file.endswith('.doc') or file.endswith('.docx') or file.endswith('.xls') or file.endswith('.xlsx'):
            with open(local_folder + '/' + file, 'rb') as f:
                ftp.storbinary('STOR ' + file, f)
                
                ftp = ftpConnection.connect_ftp(FTP_HOST, FTP_USER, FTP_PASSWORD)

upload_files(ftp, folder_path)

ftp.dir() 

ftp.quit()
