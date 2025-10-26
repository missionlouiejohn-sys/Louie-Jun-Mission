from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

# Temporary in-memory storage (resets when app restarts)
students = [
    {"name": "Your Name", "year": 10, "section": "Zechariah"}
]

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
                margin: 15px;
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
        <a href="/students">📚 View All Students</a>
        <a href="/add_student">➕ Add Student</a>
    </body>
    </html>
    """

@app.route('/students')
def list_students():
    student_cards = ""
    for s in students:
        student_cards += f"""
        <div class="card">
            <p><strong>Name:</strong> {s['name']}</p>
            <p><strong>Year:</strong> {s['year']}</p>
            <p><strong>Section:</strong> {s['section']}</p>
        </div>
        """

    return f"""
    <html>
    <head>
        <title>Student List</title>
        <style>
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #FF9A8B, #FF6A88, #FF99AC);
                color: #333;
                text-align: center;
                padding: 50px;
                margin: 0;
            }}
            h2 {{
                font-size: 2.5em;
                color: white;
            }}
            .card {{
                background: white;
                border-radius: 20px;
                padding: 20px;
                width: 250px;
                margin: 20px auto;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                animation: fadeIn 0.8s ease;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                color: white;
                text-decoration: underline;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h2>👩‍🎓 Student List</h2>
        {student_cards}
        <a href="/add_student">➕ Add Another Student</a><br>
        <a href="/">← Back to Home</a>
    </body>
    </html>
    """

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        year = request.form.get('year')
        section = request.form.get('section')

        if name and year and section:
            students.append({"name": name, "year": year, "section": section})
            return redirect('/students')

    return """
    <html>
    <head>
        <title>Add Student</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #43CBFF, #9708CC);
                color: white;
                text-align: center;
                padding: 100px;
                margin: 0;
            }
            h2 {
                font-size: 2.5em;
            }
            form {
                background: white;
                color: #333;
                border-radius: 20px;
                padding: 30px;
                display: inline-block;
                text-align: left;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }
            label {
                display: block;
                margin: 10px 0 5px;
                font-weight: bold;
            }
            input {
                width: 100%;
                padding: 10px;
                border-radius: 10px;
                border: 1px solid #ccc;
                margin-bottom: 15px;
                font-size: 1em;
            }
            button {
                width: 100%;
                padding: 10px;
                border: none;
                border-radius: 20px;
                background: linear-gradient(135deg, #9708CC, #43CBFF);
                color: white;
                font-size: 1.1em;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: linear-gradient(135deg, #43CBFF, #9708CC);
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
        <h2>➕ Add a New Student</h2>
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" name="name" required>

            <label for="year">Year:</label>
            <input type="number" name="year" required>

            <label for="section">Section:</label>
            <input type="text" name="section" required>

            <button type="submit">Add Student</button>
        </form>
        <a href="/">← Back to Home</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
