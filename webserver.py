from flask import Flask

from threading import Thread

app = Flask('')


@app.route('/')
def home():
    s = """<h1> General commands: </h1>
  <ul> > <strong>!help</strong> - displays all the available commands </ul>
  <ul> > <strong>!play [keywords]</strong> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused </ul>
  <ul> > <strong>!queue</strong> - displays the current music queue </ul>
  <ul> > <strong>!skip</strong> - skips the current song being played </ul>
  <ul> > <strong>!clear</strong> - Stops the music and clears the queue </ul>
  <ul> > <strong>!leave</strong> - Disconnected the bot from the voice channel </ul>
  <ul> > <strong>!pause</strong> - pauses the current song being played or resumes if already paused </ul>
  <ul> > <strong>!resume</strong> - resumes playing the current song </ul>
  <ul> > <strong>!current</strong> - displays the current song </ul>
  <ul> > <strong>!gif [query]</strong> - get a gif from giphy and send it to the current channel </ul>
  <strong>\WARNING/ The prefix for all commands is '!'</strong>
  <h5>I'm alive</h5>
  """
    return s


def run():

    app.run(host='0.0.0.0', port=8080)


def keep_alive():

    t = Thread(target=run)

    t.start()
