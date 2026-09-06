from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        nev = request.form["nev"]
        kor = int(request.form["kor"])
        magassag = float(request.form["magassag"])
        suly = float(request.form["suly"]
        )
        nem = request.form["nem"]
        aktivitas = float(request.form["aktivitas"])

        magassag_meter = magassag / 100
        bmi = suly / (magassag_meter * magassag_meter)

        if bmi < 18.5:
            kategoria = "Alacsony testsúly"
            szin = "blue"
        elif bmi < 25:
            kategoria = "Normál testsúly"
            szin = "green"
        elif bmi < 30:
            kategoria = "Túlsúly"
            szin = "orange"
        else:
            kategoria = "Elhízás"
            szin = "red"

        if nem == "ferfi":
            alapanyagcsere = 10 * suly + 6.25 * magassag - 5 * kor + 5
        else:
            alapanyagcsere = 10 * suly + 6.25 * magassag - 5 * kor - 161

        kaloria = alapanyagcsere * aktivitas

        return f"""
        <!DOCTYPE html>
        <html lang="hu">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Egészség kalkulátor</title>

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

                .details {{
                    font-size: 18px;
                    margin: 8px 0;
                }}

                .category {{
                    font-size: 24px;
                    margin: 25px 0 30px;
                    color: {szin};
                    font-weight: bold;
                }}

                .calories {{
                    font-size: 28px;
                    font-weight: bold;
                    margin: 25px 0;
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

                <p class="details">📏 Magasság: {magassag} cm</p>
                <p class="details">⚖️ Súly: {suly} kg</p>
                <p class="details">🎂 Életkor: {kor} év</p>

                <div class="category">{kategoria}</div>

                <p>Napi becsült kalóriaszükségleted:</p>

                <div class="calories">
                    🔥 {round(kaloria)} kcal
                </div>

                <a href="/">Új számítás</a>

            </div>

        </body>
        </html>
        """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)