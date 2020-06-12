import flask
from ViridaePy.py import GetAll_AccountIds_ForAllAccountNames

async def waitOnGameCall():


app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/api/game', methods=['GET'])
async def gameDetailsDto():
    gameObject =  ViridaePy.GetAll_AccountIds_ForAllAccountNames() #run Other File
    return await {'game': gameObject}

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)

#Error Handling Responses!
@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("400.html"), 400)

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(render_template("500.html"), 500)

app.run()