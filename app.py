from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Project</h1>

    <form action="/submit" method="post">
        <input type="text" name="name" placeholder="Enter Name">
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return f"Hello {name}! Data received successfully."

if __name__ == "__main__":
    app.run(debug=True)