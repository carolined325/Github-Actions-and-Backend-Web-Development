from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """Hello, world! <a href="/add">Add</a> <a href="/subtract">Subtract</a> <a href="/multiply">Multiply</a>"""

@app.route("/add")
def add():
    page = """
    <form action=/add method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form> 
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The sum is {a+b}</p>"
    except:
        pass

    return f"""{page} <a href="/">Home</a> <a href="/subtract">Subtract</a> <a href="/multiply">Multiply</a>"""

@app.route("/subtract")
def subtract():
    page = """
    <form action=/subtract method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form> 
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The difference is {a-b}</p>"
    except:
        pass

    return f"""{page} <a href="/">Home</a> <a href="/add">Add</a> <a href="/multiply">Multiply</a>"""

@app.route("/multiply")
def multiply():
    page = """
    <form action=/multiply method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form> 
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The product is {a*b}</p>"
    except:
        pass

    return f"""{page} <a href="/">Home</a> <a href="/subtract">Subtract</a> <a href="/add">Add</a>"""
