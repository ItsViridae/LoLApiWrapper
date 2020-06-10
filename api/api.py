import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('api/test', methods=['GET', 'POST'])
def testSucessfulResponse():
    headers = {"Content-Type": "application/json"}
    return make_response('test worked!',
                         200,
                         headers=headers)

@app.route('api/GameDtoEndpoint', methods=['GET', 'POST'])
def gameDetailsDto():
    headers = {"Content-Type": "application/json"}
    return make_response('Game Object summary (Testing)',
                         200,
                         headers=headers)

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