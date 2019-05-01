# Site-Monitor
Python script to monitor websites and email you if the site is down.

## What I Learned
* How to build a script to monitor website.
* How to use smtplib to send emails.
* How to interact with Linode servers through Linode API.
* Logging Basics

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python3.7
* pip3

### Installing
A step by step set of instructions to get a development environment running.

Setup configuration file for email services and your linode token.
```
sudo nano /etc/config.json
```
```
{
        "EMAIL_USER":"email",
        "EMAIL_PASS":"password",
        "EMAIL_DEFAULT_SENDER":"email",
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
python3 -m venv monitor_env
```
Activate your virtual environment.
```
source monitor_env/bin/activate
```
Install the Pyhon dependencies.
```
pip install -r requirements.txt
```

To automate this script to check your websites you can do the following.

Find Python environment path, something like '~/Site-Monitor/monitor_env/bin/python'
which python

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
* Script built based on [this Flask script](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Site-Monitor/monitor.py) from YouTube by [Corey Scafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g).
