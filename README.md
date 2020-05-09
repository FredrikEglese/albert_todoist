# Albert Todoist

This is an extension for [Albert Launcher](https://albertlauncher.github.io/) which adds tasks to your todoist tasklist.

## Dependencies/Installing

This extension uses [IFTTT](https://ifttt.com/) (more specifically [webhooks](https://ifttt.com/maker_webhooks)) and [Todoist](https://todoist.com/) so you will need an acount with each to get started.

### Webhooks

Go to [IFTTT Webhooks](ifttt.com/maker_webhooks) -> Documentation.

Coppy your key from the top of the page and paste it into the variable accesskey in the `__init__.py` file (near the bottom) or the `accesskey.txt` configfile if I have sorted that out yet. 

### Making the IFTTT applet

Create a new maker webhook aplet with the following atributes:
* Event name: todoist_new_event
* Task content: Value1
* Due date: Value2
