# Albert Todoist Python Extension

This is an extension for the [Albert Launcher](https://albertlauncher.github.io/) which adds tasks to your todoist tasklist.

Rather than having to open the website or app to add a task to todoist, now you just have to launch Albert (crtl + space), type `td <task>` and press enter then your task will be sent to your todoist inbox with a due date of today (or tomorrow if you select that option in the list).

I built this so that I could simplify the capture phase of my task workflow, reducing any friction for getting ideas down.

## Dependencies/Installing

This extension uses [IFTTT](https://ifttt.com/) (more specifically [webhooks](https://ifttt.com/maker_webhooks)) and [Todoist](https://todoist.com/) so you will need an acount with each to get started.

### Webhooks

Go to [IFTTT Webhooks](https://ifttt.com/maker_webhooks) -> Documentation.

Coppy your key from the top of the page and paste it into the variable accesskey in the `__init__.py` file (near the bottom) or the `accesskey.txt` configfile if I have sorted that out yet. 

### Making the IFTTT applet

Create a new maker webhook aplet with the following atributes:
* Event name: todoist_new_event
* Task content: Value1
* Due date: Value2

## Future Improvements

* Error handling
* Date selection past just today or tomorrow
* Investigate if I really need IFTTT
