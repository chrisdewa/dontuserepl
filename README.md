# dontuserepl

Let's face it, repl.it is one of the best places to develop, test and run code. As such, it's been popular for small discord bots for a couple of years now. Many people dislike the platform for various reasons, mainly, low resources, public code, etc, and they'll tell you to stop using it, however it remains a good place to start out and try new code easily.

The most popular way to run a discord bot on repl is to create a webserver on a different thread and configure a monitor service like uptimerobot.com to ping the server every five minutes or so.

Even though this is very simple to do, i feel bored by it, that's why i wrote this simple library.

# How to use it:
Making your bot 24/7 is extremely easy with `dontuserepl`.

1) Go to https://uptimerobot.com/, open an account and login.
2) Go to "My settings" and scroll to "API Settings".
3) Create and copy a "Main API Key"
4) Go to your repl and add the key as a secret
5) Add the snippet below to your main.py file.
```python
import os
from dontuserepl import lazy_setup
key = os.getenv('uptimerobot_api_key')  # use the name of the secret from step 4
lazy_setup(key)
```
6) That's it, `lazy_setup` runs a minimal aiohttp server on port 8080 and configures a monitor for the script.



