# Site-Monitor
Python script to monitor websites and email you if the site is down.

## What I Learned
* How to write a script to monitor my websites.
* How to use smtplib to send emails.
* How to interact with Linode servers through Linode API.
* Logging Basics

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python3.6+
* pip3

### Installing

Setup configuration file for email services and your linode token.
```
sudo nano ~/.bash_config
```
```
{
        "MAIL_USERNAME":"email",
        "MAIL_PASSWORD":"password",
        "MAIL_DEFAULT_SENDER":"email",
        "LINODE_TOKEN":"token"
}
```
Clone the repository onto your machine.
```
git clone https://github.com/itzliu/Site-Monitor.git
```
Change directory into the project directory folder.
```
cd Site-Monitor
```
Create a virtual environment for the app.
```
python3 -m venv venv
```
Activate your virtual environment.
```
source venv/bin/activate
```
Install the Pyhon dependencies.
```
pip install requests
pip install linode_api4
```

To automate this script to check your websites you can do the following.

Find Python environment path. (something like '~/Site-Monitor/monitor_env/bin/python')
```
which python
```
Open cron
```
crontab -e
```
Press 'i' to enter edit mode and add the cron script.
```
*/10 * * * * [environement path] [monotor.py path]
```
Press 'Esc' to exit edit mode and type in ':wq' to write and quit.

## Running Tests
N/a

## Built With
* smtplib
* requests
* logging
* linode_api4

## Authors
* Harry Liu

## Acknowledgements
* Script built based on [this monitor script](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Site-Monitor/monitor.py) from YouTube by [Corey Scafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g).
