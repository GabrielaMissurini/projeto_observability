import http.client
import logging

from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

import prometheus_client as prom
import random
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge("quantidade_usuarios_online",
                                        "Número de usuários online no momento")

def parametros_endpoint():
    time.sleep(random.randint(1,10))
    quantidade_usuarios_online.set(random.randint(1,100))

@app.route('/renda-fixa')
def renda_fixa():
    app.logger.info('%s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path)
    app.logger.info("Acessando Renda Fixa")
    parametros_endpoint()
    if random.randint(0,1) == 0:
       return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Renda fixa")

@app.route('/renda-variavel')
def renda_variavel():
    app.logger.info('%s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path)
    parametros_endpoint()
    return render_template("lista.html", titulo="Renda variavel")

@app.route('/cripto')
def cripto():
    app.logger.info('%s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path)
    parametros_endpoint()
    return render_template("lista.html", titulo="Cripto")

@app.route('/fii')
def fii():
    app.logger.info('%s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path)
    parametros_endpoint()
    return render_template("lista.html", titulo="FIIs")


if __name__ == "__main__":
    app.run(host="0.0.0.0")