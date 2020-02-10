# Site Monitor
Python script to monitor websites. If a server is found to be down a email will be sent to the specified user and the server will be reset. Script is currently for use with only Linode servers but compatability with other service provider APIs can be added.

## Utilizes
* Cron
* Linode API
* Python SMTP Library
* Logging

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Requirements
* Python3.6+
* pip3
* Google App Password: https://myaccount.google.com/apppasswords

### Installing

Setup configuration file for email services and your linode token.
```
sudo nano ~/.bash_config
```
```
{
        "MAIL_USERNAME":"email",
        "MAIL_PASSWORD":"google app password",
        "LINODE_TOKEN":"token"
}
```
```
git clone https://github.com/itzliu/site-monitor.git
cd site-monitor
python3 -m venv venv
source venv/bin/activate
pip install requests
pip install linode_api4
python monitor.py
```

To automate this script to check your websites periodically you can do the following.

Find Python environment path. (something like '~/site-monitor/venv/bin/python')
```
which python
```
Open cron
```
crontab -e
```
Add this to the cron script to run the monitor script every 10 minutes.
```
*/10 * * * * . $HOME/.bash_config && [environement path] [monotor.py path]
```

## Authors
* Harry Liu

## Acknowledgements
* Script built based on [this monitor script](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Site-Monitor/monitor.py) from YouTube by [Corey Scafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g).
