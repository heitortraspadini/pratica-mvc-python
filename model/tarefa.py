from model.database import Database
 
class Tarefa:
    def __init__(self, titulo, data_conclusao = None, id= None):
        self.titulo = titulo
        self.id = id
        self.data_conclusao = data_conclusao
 
    def salvar_tarefa(self):
        """Salva uma nova tarefa no banco de dados!?"""
        db = Database()
        db.conectar()
 
        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()
 
    def listar_tarefa():
        """Retornar uma lista com todas as tarefas..."""
        db = Database()
        db.conectar()
 
        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
   
    @staticmethod
    def apagar_tarefa(idTarefa):
        """Apaga uma tarefa cadastrada no banco de dados?"""
        db = Database()
        db.conectar()
        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa ser uma tupla!
        db.executar(sql, params)
        db.desconectar()
 
    def atualizar_tarefa(self):
        """Atualiza uma tarefa existente no banco de dados."""
        db = Database()
        db.conectar()
        sql = "UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s"
        params = (self.titulo, self.data_conclusao, self.id)
        db.executar(sql, params)
        db.desconectar()
 
    @staticmethod
    def buscar_por_id(idTarefa):
        """Busca uma tarefa pelo ID no banco de dados."""
        db = Database()
        db.conectar()
 
        sql = "SELECT id, titulo, data_conclusao FROM tarefa WHERE id = %s"
        params = (idTarefa,)
        resultado = db.consultar(sql, params)
        db.desconectar()
 
        if resultado:
            id, titulo, data_conclusao = resultado[0]["id"], resultado[0]["titulo"], resultado[0]["data_conclusao"]
            return Tarefa(titulo=titulo, data_conclusao=data_conclusao, id=id)
        return None