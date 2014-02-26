A Google App Engine application for sanitising Facebook vcal feeds for import into Google Calendar.

### Configuration
* Edit *events.py* and replace *[YOUR_EVENTS_URL]* with the url of your private Facebook events calendar feed.
* Edit *birthdays.py* and replace *[YOUR_BIRTHDAYS_URL]* with the url of your private Facebook birthdays calendar feed.
* Edit *app.yaml*, replace *[YOUR_APP_ID]* with your GAE application ID, replace both *[YOUR_PATH]* with different obscure string values; the events and birthday calendars will be accesible on these paths (choosing obscure and random paths make it harder for people to guess the paths and gain access to your calendars).

### Installation
Install using the Google App Engine Python SDK - https://developers.google.com/appengine/
