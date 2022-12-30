# WebDeck
A web based macro/stream deck for your enjoyment

## What is WebDeck?
It's a small project of mine that I decided to work on for fun.  It uses Python and Flask to run the web server.

## How do I use it?
1.  Clone this repository
2.  Install everything in requirements.txt:
        ```
        pip install -r requirements.txt
        ```
3.  Run `app.py`
4.  Connect to the server on any device!

To change any settings, you can edit `settings.json` to your liking.
At the moment, I only implemented 2 functions: `mute-mic` and `mute`
These mute the microphone and system output respectively.

# Compatability
This only works on Windows, as it uses some powershell snippets to access windows system volume controls.  Feel free to fork and make a linux/macos variant though!
