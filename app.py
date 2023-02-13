from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/renda-fixa')
def renda_fixa():
    return render_template("lista.html", título="Renda fixa")
if __name__ == "__main__":
    app.run(host="0.0.0.0")