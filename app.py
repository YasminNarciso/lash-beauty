from flask import Flask, render_template, request, render_template_string, redirect, url_for, has_app_context

#Objeto/servidor do flask
app = Flask(__name__)

app.app_context()

#rota principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cilios')
def cilios():
    return render_template('cilios.html')

@app.route('/colas')
def colas():
    return render_template('colas.html')

@app.route('/acessorios')
def acessorios():
    return render_template('acessorios.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/compra-entrega', methods=['GET', 'POST'])
def comprar1():
    if request.method == "POST":
        email = request.form.get('email')
        cep = request.form.get('cep')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        numero = request.form.get('numero')
        complemento = request.form.get('complemento')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cpf = request.form.get('cpf')
        return render_template('comprar1.html')
    
@app.route('/compra-pagamento')
def comprar2():
    return render_template('comprar2.html') 



#execução do servidor
if __name__ == "__main__":
        app.run (debug=True)

