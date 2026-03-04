from flask import Flask, jsonify

app = Flask(__name__)

mode_absence = False

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/mode-on")
def mode_on():
    global mode_absence
    mode_absence = True
    return jsonify({"mode_absence": mode_absence})

@app.route("/mode-off")
def mode_off():
    global mode_absence
    mode_absence = False
    return jsonify({"mode_absence": mode_absence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)