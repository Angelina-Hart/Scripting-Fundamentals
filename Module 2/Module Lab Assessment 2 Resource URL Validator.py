import pip
import requests

def validate_url(url):
    valid_protocols = ["http", "https", "ftp"]
    valid_fileinfo = ["html", "csv", "docx"]
    protocol = url.split("://", 1)
    extension = url.rsplit(".", 1)
    if protocol[0] in valid_protocols:
        if extension[1] in valid_fileinfo:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    url = input("Enter an Url: ")
    print(validate_url(url))
