This Python application uses `snscrape` to monitor changes in the Twitter descriptions of users listed in a text file. When a user's description changes, an alert is sent to a configured Discord Webhook.

## Requirements
* Python 3.6+
* `snscrape` : For scraping Twitter user profiles
* `requests` : For sending HTTP requests (used for Discord webhooks)

## Setup

1. Clone the repository.
``
git clone https://github.com/clovisjohn/twitter-profiles-monitor.git
``

2. Set up your Discord Webhook URL in the main script. Replace the empty string of `webhook_url` variable at the top of the script with your Discord webhook URL

3. Add the usernames of the Twitter accounts you want to monitor in a file named `users.txt`, one username per line.

4. To start monitoring the changes, run the script with the following command:
``
python main.py
``

The script will loop indefinitely, sleeping for 3 hours between each check. If a change is detected, an alert will be sent to the Discord Webhook URL with the previous and new description.


