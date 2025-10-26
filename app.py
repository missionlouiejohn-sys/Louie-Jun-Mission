from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Welcome to My Flask API</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #74ABE2, #5563DE);
                color: white;
                text-align: center;
                padding: 100px;
                margin: 0;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2em;
                margin-top: 0;
            }
            a {
                display: inline-block;
                margin-top: 30px;
                padding: 10px 20px;
                background: white;
                color: #5563DE;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }
            a:hover {
                background: #e0e0e0;
            }
        </style>
    </head>
    <body>
        <h1>🎓 Welcome to My Flask API!</h1>
        <p>Explore student information and more.</p>
        <a href="/student">View Student Info</a>
    </body>
    </html>
    """

@app.route('/student')
def get_student():
    return """
    <html>
    <head>
        <title>Student Info</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #FF9A8B, #FF6A88, #FF99AC);
                color: #333;
                text-align: center;
                padding: 100px;
                margin: 0;
            }
            h2 {
                font-size: 2.5em;
                color: white;
            }
            .card {
                background: white;
                border-radius: 20px;
                padding: 30px;
                width: 300px;
                margin: 0 auto;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                animation: fadeIn 0.8s ease;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            p {
                font-size: 1.1em;
                margin: 10px 0;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                color: white;
                text-decoration: underline;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h2>👩‍🎓 Student Information</h2>
        <div class="card">
            <p><strong>Name:</strong> Your Name</p>
            <p><strong>Grade:</strong> 10</p>
            <p><strong>Section:</strong> Zechariah</p>
        </div>
        <a href="/">← Back to Home</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
