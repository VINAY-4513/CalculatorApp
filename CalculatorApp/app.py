from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        a = float(request.form["num1"])
        b = float(request.form["num2"])
        op = request.form["operation"]

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = "Cannot divide by zero" if b == 0 else a / b

    return render_template_string("""
    <html>
    <head>
        <title>Python Calculator</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: lightblue;
                padding: 50px;
            }
            .box {
                background: white;
                padding: 30px;
                width: 300px;
                margin: auto;
                border-radius: 15px;
            }
            input, select, button {
                padding: 10px;
                margin: 10px;
                width: 85%;
            }
            button {
                background: green;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Calculator</h1>
            <form method="POST">
                <input type="number" step="any"
                       name="num1" placeholder="First Number" required>

                <input type="number" step="any"
                       name="num2" placeholder="Second Number" required>

                <select name="operation">
                    <option value="+">Addition (+)</option>
                    <option value="-">Subtraction (-)</option>
                    <option value="*">Multiplication (*)</option>
                    <option value="/">Division (/)</option>
                </select>

                <button type="submit">Calculate</button>
            </form>
            <h2>Result: {{ result }}</h2>
        </div>
    </body>
    </html>
    """, result=result)

if __name__ == "__main__":
    app.run(debug=True)