import snscrape.modules.twitter as sntwitter
import json
import time
import requests

# Discord Webhook URL
webhook_url = ''

# load previous data
try:
    with open('users.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {}


def send_alert(username, previousDescription, newDescription):
    data = {}
    data["embeds"] = [
        {
            "title" : "Description Changed",
            "description" : username,
            "color" : 16711680,
            "fields" : [
                {"name": "Previous Description", "value": previousDescription, "inline": False},
                {"name": "Current Description", "value": newDescription, "inline": False}
            ]
        }
    ]
    requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    
while True:
    with open('users.txt', 'r') as f:
        usernames = f.read().splitlines()

    for username in usernames:
        scraper = sntwitter.TwitterUserScraper(username)
        if scraper.entity:
            description = scraper.entity.description
            if username not in user_data:
                user_data[username] = {'description': description, 'time': time.time()}
                print(f'Added {username} to user_data, current description: {description}')
            elif description != user_data[username]['description']:
                # description changed, send discord message
                print(f'Description changed for {username}, sending alert')
                send_alert(username, user_data[username]['description'], description)
            
                # update description in our data
                user_data[username]['description'] = description
                user_data[username]['time'] = time.time()

    # store updated data
    with open('users.json', 'w') as f:
        json.dump(user_data, f)

    # sleep for 3 hours
    print('Sleeping for 3 hours')
    time.sleep(3*60*60)