from flask import Flask, render_template, request

app = Flask(__name__)

def printRoman(number): 
    numerals={1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C",
         90:"XC", 50:"L", 40:"XL",10:"X", 9: "IX",  5:"V", 4:"IV", 1:"I"}          
    result=""
    for value, numeral in numerals.items():
        while number >= value:
            result += numeral
            number -= value
    return result

@app.route ("/", methods=["GET"])
def main_get():
    return render_template("index.html", developer_name="E2061-OmerKaan", not_valid=False)   

@app.route ("/", methods=["POST"])
def main_post():
    num = request.form["number"]
    if (not num.isdecimal()) or (not (0<int(num)<4000)):
        return render_template("index.html", developer_name="E2061-OmerKaan", not_valid=True)
    
    return render_template("result.html", developer_name="E2061-OmerKaan", number_decimal=num, number_roman=printRoman(int(num)))

if (__name__) == "__main__":
    app.run(host="0.0.0.0", port=80)

