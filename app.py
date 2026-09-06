from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        nev = request.form["nev"]
        magassag = float(request.form["magassag"])
        suly = float(request.form["suly"])

        magassag_meter = magassag / 100
        bmi = suly / (magassag_meter * magassag_meter)

        if bmi < 18.5:
            kategoria = "Alacsony testsúly"
        elif bmi < 25:
            kategoria = "Normál testsúly"
        elif bmi < 30:
            kategoria = "Túlsúly"
        else:
            kategoria = "Elhízás"

        return f"""
        <!DOCTYPE html>
        <html lang="hu">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>BMI eredmény</title>

            <style>
                body {{
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #f2f4f7;
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }}

                .result {{
                    background: white;
                    width: 100%;
                    max-width: 420px;
                    padding: 35px;
                    border-radius: 20px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }}

                h1 {{
                    margin-bottom: 10px;
                }}

                .bmi {{
                    font-size: 50px;
                    font-weight: bold;
                    margin: 20px 0 10px;
                }}

                .category {{
                    font-size: 24px;
                    margin-bottom: 30px;
                }}

                a {{
                    display: block;
                    padding: 13px;
                    background: #222;
                    color: white;
                    text-decoration: none;
                    border-radius: 10px;
                    font-size: 17px;
                }}
            </style>
        </head>

        <body>

            <div class="result">

                <h1>Szia, {nev}! 👋</h1>

                <p>A BMI értéked:</p>

                <div class="bmi">{round(bmi, 1)}</div>

                <div class="category">{kategoria}</div>

                <a href="/">Új számítás</a>

            </div>

        </body>
        </html>
        """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)