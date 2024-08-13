print("Alô mundo!")

#flask: módulo Flask: classe
from flask import Flask, render_template

from matematica import Matematica

from timefut import TimeFut

# App: obejeto (é uma instância)
# flask(): é o construtor da classe Flask
# name: é uma variável especial em Python que definida como o nome do módulo atual. (quando vc passa name para o construtor do Flask, ele)

app = Flask(__name__)
@app.route('/inicio')

# def: função (definição de uma função).
# ola: 
def ola():
    return "Olá Mundo!"
#Chma a função de esecução do flask:


@app.route('/olamundo')
def mostrar():
    return render_template('pagina.html')

@app.route('/listatimes')
def listar_times():
    t1 = TimeFut('Palmeiras',10)
    t2 = TimeFut('Botafogo',7)
    t3 = TimeFut('Flamego',9)
    lista = [t1,t2,t3]
    return render_template('listatimes.html',times=lista)

                  
@app.route('/calculosoma')
def calcular():
    mat = Matematica(5,7)
    resposta = mat.somar()
    return render_template('calculo.html',resultado=resposta)
app.run(debug=True)