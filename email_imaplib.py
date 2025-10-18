import imaplib
from imaplib import IMAP4
import email
from email.header import decode_header

username = "abc@outlook.com"
password = "password"


imap = imaplib.IMAP4_SSL(host="imap-mail.outlook.com", port= 993, ssl_context= None, timeout= None)
imap.login(username, password)
print(imap.list())
