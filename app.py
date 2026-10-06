
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>SkillMatch</title></head>
        <body style="font-family: Arial; text-align: center; padding: 60px;">
            <h1>Welcome to SkillMatch!</h1>
            <h2>Skill Job Recommender System</h2>
            <p>Your website is running successfully.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)