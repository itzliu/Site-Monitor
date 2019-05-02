import os
import smtplib
import requests
import logging
from linode_api4 import LinodeClient, Instance

# Specify website name, url, and linode-server.

WEBSITES = [
    {
        'name': 'iamharryliu',
        'url': 'https://www.iamharryliu.com/',
        'linode-server': 'flask-server'
    },
    {
        'name' : 'Google',
        'url' : 'https://www.google.ca/', 
    },
    {
        'name' : 'Youtube',
        'url' : 'https://www.youtube.com/'
    }
]
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_DEFAULT_SENDER = os.environ.get('EMAIL_DEFAULT_SENDER')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

logging.basicConfig(filename='/tmp/logs/site-monitor.log',
                    level=logging.INFO,
                    format='%(asctime)s\t%(levelname)s\t%(message)s')

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = f'{website["name"]} SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'
        logging.info('Sending Email...')
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

def reboot_server():
    if 'linode-server' in website:
        reboot_linode_server()

def reboot_linode_server():
    client = LinodeClient(LINODE_TOKEN)
    server_id = get_linode_server_id(client)
    my_server = client.load(Instance, server_id)
    my_server.reboot()
    logging.info('Attempting to reboot server...')

def get_linode_server_id(client):
    for linode in client.linode.instances():
        if linode.label == website['linode-server']:
            server_id = linode.id
    return server_id

for website in WEBSITES:
    try:
        r = requests.get(website['url'], timeout=5)
        if r.status_code != 200:
            logging.info(f'{website["name"]} is DOWN!')
            notify_user()
            reboot_server()
        else:
            logging.info(f'{website["name"]} is UP')
    except Exception as e:
        logging.info(f'{website["name"]} is DOWN!')
        notify_user()
        reboot_server()