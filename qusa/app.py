from quart import Quart, websocket

app = Quart(__name__)

@app.route("/")
async def hello():
    return await render_template("index.html")

@app.route("/api/helloworld")
async def json_hw():
    return {"hello": "world"}

@app.route("/api/hellomoon")
async def json_hm():
    return {"hello": "moon"}

if __name__ == "__main__":
    app.run()
