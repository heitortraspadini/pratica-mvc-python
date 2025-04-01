from unittest.runner import _ResultClassType
from flask import Flask, render_template, request, url_for, redirect
from model.tarefa import Tarefa
 
app = Flask(__name__)
 
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        titulo = request.form["titulo"]
        data_conclusao = request.form["data_conclusao"]
        tarefa = Tarefa(titulo = titulo, data_conclusao = data_conclusao)
        tarefa.salvar_tarefa()
        return redirect(url_for("index"))
 
    tarefas = Tarefa.listar_tarefa()
    return render_template("index.html", tarefas=tarefas, title="Minhas Tarefas")
 
@app.route("/delete/<int:idTarefa>")
def delete(idTarefa):
    Tarefa.apagar_tarefa(idTarefa)
    return redirect(url_for("index"))
 
@app.route("/update/<int:idTarefa>", methods=["GET", "POST"])
def edit(idTarefa):
    if request.method == "POST":
        # Atualizar a tarefa no banco de dados
        titulo = request.form["titulo"]
        data_conclusao = request.form["data_conclusao"]
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao, id=idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for("index"))
    
    tarefa = Tarefa.buscar_por_id(idTarefa)
    return render_template(
        "update.html", 
        tarefa=tarefa, 
        title="Editando tarefa | Minhas Tarefas"
        )
    