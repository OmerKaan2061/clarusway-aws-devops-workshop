from flask import Flask, render_template, request
import romen_numerals

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        num = request.form["number"]
        if romen_numerals.convert(num):
            return render_template("result.html", developer_name="E2021-Gokhan",\
                 number_decimal=num,number_roman=romen_numerals.convert(num))
        else:
            return render_template("index.html",developer_name="E2021-Gokhan", not_valid=True)
        
    else:
        return render_template("index.html", developer_name="E2021-Gokhan")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=80)
