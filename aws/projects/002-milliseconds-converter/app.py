from flask import Flask, render_template, request

app = Flask(__name__)

def convert (millisecond):
    hour_in_millisecond = 60*60*1000
    hours = millisecond // hour_in_millisecond
    millisecond_left = millisecond % hour_in_millisecond

    minute_in_millisecond = 60*1000
    minutes = millisecond_left // minute_in_millisecond
    millisecond_left %= minute_in_millisecond

    seconds = millisecond_left // 1000

    return f'{hours} hour/s'*(hours!=0) + f'{minutes} minute/s' *(minutes!=0) + f'{seconds} second/s' * (seconds !=0) or f'just {millisecond} milisecond/s'

print(convert(55))

@app.route('/', methods=['GET'])
def main_get():
    return (render_template('index.html', developer_name='OmerKaan', not_valid= False))

@app.route('/', methods = ['POST'])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='OmerKaan', not_valid=True)
    if not (0 < int(alpha)):
        return render_template('index.html', developer_name='OmerKaan', not_valid=True)
    return render_template('result.html', developer_name='OmerKaan', milliseconds = int(alpha), result=convert(int(alpha)))

if (__name__) == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=80)