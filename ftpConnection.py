import ftplib

def ftp_connection(ftp_host, ftp_username, ftp_password):
    ftp = ftplib.FTP(ftp_host)
    ftp.login(ftp_username, ftp_password)
    return ftp