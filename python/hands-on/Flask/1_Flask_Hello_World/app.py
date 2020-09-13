from flask import Flask

app = Flask(__name__)


@app.route("/") #burası decorator. Bununla yolladigimiz reqıeste nasil cevap verecegini tanimliyoruz. Yazmasak not found hatasi verir.
def head():
    return "Hello World!"


@app.route("/second")
def second():
    return "This is the second page"


@app.route("/third/subthird")
def third():
    return "This is sub-third of third"


@app.route("/forth/<string:id>") #dinamik id yapilari icin tanimlandi.
def forth(id):
    return f"Id of this page is {id}"


if __name__ == '__main__': #ana dosya diger dosyaları calistiracagi icin ana dosyada calisip calismadigimiiz kontrol ediyor
    app.run(debug = True) # bu sayfanin hatalari bize gösterecek sekilde calismasini sagliyor

