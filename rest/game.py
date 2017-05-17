from flask import Flask

app = Flask(__name__)

@app.route("/game/start")
def start(setup):
	pass
@app.route("/game/stop")
def stop():
	pass
@app.route("/game/pause")
def pause():
	pass
@app.route("/game/map")
def get_map():
	pass

@app.route("/")
def hello():
	return "Hello world"

if __name__ == "__main__":
  app.run()