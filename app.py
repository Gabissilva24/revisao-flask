from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/revisao')
def revisao():
    nome = 'Gabriele'
    return render_template('variaveis.html', idade=18, nome=nome)

@app.route('/revisao/<nome>/<int:idade>')
def parametros(nome,idade):
    return render_template('variaveis.html', idade=idade, nome=nome)

@app.route('/produtos/cadastrar')
def cadastrar_produtos():
    return render_template('produtos/form-produto.html')


# ------- Tem que ser a ultima coisa!
if __name__ == '__main__':
    app.run(debug=True)