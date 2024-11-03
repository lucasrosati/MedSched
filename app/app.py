import mysql.connector
import os

# Configurações de conexão com o banco de dados
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '3306'),
    'user': os.getenv('DB_USER', 'medsched_user'),
    'password': os.getenv('DB_PASSWORD', 'MedSched123!'),
    'database': os.getenv('DB_NAME', 'medsched_db')
}

# Função auxiliar para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Funções CRUD para o contexto de consultas médicas
def inserir_consulta():
    id_paciente = input("Digite o ID do paciente: ")
    id_medico = input("Digite o ID do médico: ")
    data_consulta = input("Digite a data da consulta (YYYY-MM-DD HH:MM:SS): ")
    motivo = input("Digite o motivo da consulta: ")

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Consulta (id_paciente, id_medico, data_consulta, motivo) VALUES (%s, %s, %s, %s)", 
        (id_paciente, id_medico, data_consulta, motivo)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("Consulta inserida com sucesso!")

def atualizar_consulta():
    id_consulta = input("Digite o ID da consulta a ser atualizada: ")
    id_paciente = input("Digite o novo ID do paciente: ")
    id_medico = input("Digite o novo ID do médico: ")
    data_consulta = input("Digite a nova data da consulta (YYYY-MM-DD HH:MM:SS): ")
    motivo = input("Digite o novo motivo da consulta: ")

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Consulta SET id_paciente=%s, id_medico=%s, data_consulta=%s, motivo=%s WHERE id_consulta=%s", 
        (id_paciente, id_medico, data_consulta, motivo, id_consulta)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("Consulta atualizada com sucesso!")

def consultar_consultas():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT Consulta.*, Paciente.nome AS paciente_nome, Medico.nome AS medico_nome 
        FROM Consulta 
        JOIN Paciente ON Consulta.id_paciente = Paciente.id_paciente 
        JOIN Medico ON Consulta.id_medico = Medico.id_medico
    """)
    consultas = cursor.fetchall()
    cursor.close()
    connection.close()
    
    print("\nConsultas agendadas:")
    for consulta in consultas:
        print(f"ID: {consulta['id_consulta']}, Paciente: {consulta['paciente_nome']}, Médico: {consulta['medico_nome']}, Data: {consulta['data_consulta']}, Motivo: {consulta['motivo']}")
    print()

def excluir_consulta():
    id_consulta = input("Digite o ID da consulta a ser excluída: ")

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Consulta WHERE id_consulta = %s", (id_consulta,))
    connection.commit()
    cursor.close()
    connection.close()
    print("Consulta excluída com sucesso!")

# Menu principal
def menu():
    while True:
        print("\nEscolha uma operação:")
        print("1. Inserir consulta")
        print("2. Atualizar consulta")
        print("3. Consultar dados de consultas (com junção)")
        print("4. Excluir consulta")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1':
            inserir_consulta()
        elif escolha == '2':
            atualizar_consulta()
        elif escolha == '3':
            consultar_consultas()
        elif escolha == '4':
            excluir_consulta()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
