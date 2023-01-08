import os
import ftplib

# Credentials for the public FTP Server
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"  # it may change depending on the public FTP server

folder_path = 'C:\\Users\\HP\\Desktop\\Files'

def upload_files(ftp, local_folder):
    files = os.listdir(local_folder)
    for file in files:
        if file.endswith('.doc') or file.endswith('.docx') or file.endswith('.xls') or file.endswith('.xlsx'):
            with open(local_folder + '/' + file, 'rb') as f:
                ftp.storbinary('STOR ' + file, f)
            print(file + " uploaded successfully!")    
                

# connect to FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASSWORD)

# upload files from local folder to FTP server
upload_files(ftp, folder_path)

# we can use ftp.dir() if we want to see our documents in realtime in FTP server
ftp.dir() 

# close FTP connection
ftp.quit()
