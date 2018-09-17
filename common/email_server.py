# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import datetime
import os
import smtplib
import time
from email import encoders
from email import utils
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.compress_utils import zip_compress, compress_rate


# noinspection PyStatementEffect,PyUnboundLocalVariable
def send(to, cc, subject, content, attachments, delete):
    user = 'email service address'
    password = 'xxx'
    server = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtplib.SMTP
    server.login(user, password)
    start = datetime.datetime.now()
    content_msg = MIMEMultipart()
    content_msg['From'] = user
    content_msg['To'] = ';'.join(to)
    content_msg['Cc'] = ';'.join(cc)
    content_msg['Subject'] = subject
    content_msg['Date'] = utils.formatdate()
    content_msg.attach(MIMEText(content.encode('UTF-8'), _charset='UTF-8'))
    content_type = 'application/octet-stream'
    maintype, subtype = content_type.split('/', 1)
    compress_files = []
    if len(attachments) > 0:
        for path in attachments:
            path = compress_attachment(path)
    if path.__contains__('.csv') is False:
        compress_files.append(path)
        attachment_file = open(path, 'rb')
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(attachment_file.read())
        attachment_file.close()
        encoders.encode_base64(file_msg)
        basename = os.path.basename(path)
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
        content_msg.attach(file_msg)
    try:
        server.sendmail(user, to + cc, content_msg.as_string())
        end = datetime.datetime.now()
        print('%s Email send successful in %s seconds. To users: %s'
              % (time.strftime('%Y-%m-%d%H:%M:%S'),
                 (end - start).seconds,
                 ",".join(to + cc)))
        try:
            attachments.extend(compress_files)
            if delete and len(attachments) > 0:
                for path in attachments:
                    os.remove(path)
        except IOError as e:
            print('Delete attachments were failed. Case: %s' % e)
    except Exception as e:
        raise RuntimeError('Send email[%s] failed. Case: %s' % (subject, e))
    finally:
        server.quit()


def compress_attachment(attachment):
    length = os.path.getsize(attachment)
    if length > 4194304:
        attachment = zip_compress(attachment)
        print('File\'s[%s] compress rate is %s%%'
              % (os.path.basename(attachment),
                 compress_rate(length, os.path.getsize(attachment)) * 100))
    return attachment
