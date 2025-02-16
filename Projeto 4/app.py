import flet as ft 
import requests
# flet permite trabalhar com interfaces gráficas dentro do Python
# request permite fazer requisições para o backend e buscar os dados lá

# URL base da API - ajuste conforme necessário 
API_BASE_URL = "http://localhost:8000/api"

def main(page: ft.Page): 
     page.title = "Exemplo"
     page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
     # Criar aluno --> aba
     # variáveis
     nome_field = ft.TextField(label="Nome")
     email_field = ft.TextField(label="Email")
     faixa_field = ft.TextField(label="Faixa")
     data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")
     # campo onde pode ser inserido texto, para exibir as mensagens de erro ou resultado
     create_result = ft.Text()

     # padrão de programação orientada a eventos
     # payload = dict
	 # nome das variáveis deve ser igual ao do backend
     def criar_aluno_click(e):
         payload = {
		    "nome": nome_field.value,
		    "email": email_field.value,
		    "faixa": faixa_field.value,
		    "data_nascimento": data_nascimento_field.value,
		 }
         # requisição para mandar para o backend
         try:
             response = requests.post(API_BASE_URL + "/", json=payload)
			 # sucesso
             if response.status_code == 200:
                 aluno = response.json()
                 # quando um aluno é criado, o backend devolve o aluno
                 create_result.value = f"Aluno criado: {aluno}"
             # erro - o mais correto é fazer mensagens diferentes para diferentes erros
             else:
                 create_result.value = f"Erro: {response.text}"
         except Exception as ex:
             create_result.value = f"Exceção: {ex}"
         # atualizar o create_result
         page.update()
         
     create_button = ft.ElevatedButton(text="Criar Aluno", on_click=criar_aluno_click)
     # criar uma coluna --> "página/aba"
     criar_aluno_tab = ft.Column(
         [
            nome_field,
            email_field,
            faixa_field,
            data_nascimento_field,
            create_result, 
            create_button
         ],
         # permitir scroll
         scroll=True
     )

     # Listar alunos --> aba
     students_table = ft.DataTable(
         columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Faixa")),
            ft.DataColumn(ft.Text("Data de nascimento")),
         ],
         rows=[],
     )
     list_result = ft.Text()
     
     # não precisou de payload porque não recebe parâmetros
     def listar_alunos_click(e):
         try:
             response = requests.get(API_BASE_URL + "/alunos/")
             if response.status_code == 200:
                 alunos = response.json()
                 # Limpa as linhas anteriores
                 students_table.rows.clear()
                 for aluno in alunos:
                     row = ft.DataRow(
                         cells=[
                            ft.DataCell(ft.Text(aluno.get("nome", ""))),
                            ft.DataCell(ft.Text(aluno.get("email", ""))),
                            ft.DataCell(ft.Text(aluno.get("faixa", ""))),
                            ft.DataCell(ft.Text(aluno.get("data_nascimento", ""))),
                         ]
                     )
                     students_table.rows.append(row)
                 list_result.value = f"{len(alunos)} alunos encontrados."
             else:
                 list_result.value = f"Erro: {response.text}"
         except Exception as ex:
            list_result.value = f"Exceção: {ex}"
         page.update()

     list_button = ft.ElevatedButton(text="Listar Alunos", on_click=listar_alunos_click)
     listar_alunos_tab = ft.Column([students_table, list_result, list_button], scroll=True)

     # Adicionar aulas --> aba
     email_aula_field = ft.TextField(label="Email do Aluno")
     qtd_field = ft.TextField(label="Quantidade de Aulas", value="1")
     aula_result = ft.Text()

     def marcar_aula_click(e):
         try:
             qtd = int(qtd_field.value)
             payload = {
                 "qtd": qtd,
                 "email_aluno": email_aula_field.value,
             }
             response = requests.post(API_BASE_URL + "/aula_realizada/", json=payload)
             if response.status_code == 200:
                 # A API retorna uma mensagem de sucesso
                 mensagem = response.json()  # pode ser uma string ou objeto
                 aula_result.value = f"Sucesso: {mensagem}"
             else:
                 aula_result.value = f"Erro: {response.text}"
         except Exception as ex:
             aula_result.value = f"Exceção: {ex}"
         page.update()

     aula_button = ft.ElevatedButton(text="Marcar Aula Realizada", on_click=marcar_aula_click)
     aula_tab = ft.Column([email_aula_field, qtd_field, aula_result, aula_button], scroll=True)

     # Progresso do aluno --> aba
     email_progress_field = ft.TextField(label="Email do Aluno")
     progress_result = ft.Text()

     def consultar_progresso_click(e):
         try:
             email = email_progress_field.value
             response = requests.get(
                 API_BASE_URL + "/progresso_aluno/", params={"email_aluno": email}
             )
             if response.status_code == 200:
                 progress = response.json()
                 progress_result.value = (
                     f"Nome: {progress.get('nome', '')}\n"
                     f"Email: {progress.get('email', '')}\n"
                     f"Faixa Atual: {progress.get('faixa', '')}\n"
                     f"Aulas Totais: {progress.get('total_aulas', 0)}\n"
                     f"Aulas necessárias para a próxima faixa: {progress.get('aulas_necessarias_para_proxima_faixa', 0)}"
                 )
             else:
                 progress_result.value = f"Erro: {response.text}"
         except Exception as ex:
             progress_result.value = f"Exceção: {ex}"
         page.update()

     progress_button = ft.ElevatedButton(text="Consultar Progresso", on_click=consultar_progresso_click)
     progresso_tab = ft.Column([email_progress_field, progress_result, progress_button], scroll=True)
     
     # Atualizar alunos --> aba
     id_aluno_field = ft.TextField(label="ID do Aluno")
     nome_update_field = ft.TextField(label="Novo Nome")
     email_update_field = ft.TextField(label="Novo Email")
     faixa_update_field = ft.TextField(label="Nova Faixa")
     data_nascimento_update_field = ft.TextField(label="Nova Data de Nascimento (YYYY-MM-DD)")
     update_result = ft.Text()

     def atualizar_aluno_click(e):
         try:
             aluno_id = id_aluno_field.value
             if not aluno_id:
                 update_result.value = "ID do aluno é obrigatório."
             else:
                 # dicionário com todos os campos que foram preenchidos
                 payload = {
                     "nome": nome_update_field.value,
                     "email": email_update_field.value,
                     "faixa": faixa_update_field.value,
                     "data_nascimento": data_nascimento_update_field.value
                 }
                 if nome_update_field.value:
                     payload["nome"] = nome_update_field.value
                 if email_update_field.value:
                     payload["email"] = email_update_field.value
                 if faixa_update_field.value:
                     payload["faixa"] = faixa_update_field.value
                 if data_nascimento_update_field.value:
                     payload["data_nascimento"] = data_nascimento_update_field.value

                 response = requests.put(API_BASE_URL + f"/alunos/{aluno_id}", json=payload)
                 if response.status_code == 200:
                     aluno = response.json()
                     update_result.value = f"Aluno atualizado: {aluno}"
                 else:
                     update_result.value = f"Erro: {response.text}"
         except Exception as ex:
             update_result.value = f"Exceção: {ex}"
         page.update()

     update_button = ft.ElevatedButton(text="Atualizar Aluno", on_click=atualizar_aluno_click)
     atualizar_tab = ft.Column(
         [
             id_aluno_field,
             nome_update_field,
             email_update_field,
             faixa_update_field,
             data_nascimento_update_field,
             update_button,
             update_result,
         ],
         scroll=True,
     )

     tabs = ft.Tabs(
         selected_index=0,
         tabs=[
             ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
             ft.Tab(text="Listar Alunos", content=listar_alunos_tab),
             ft.Tab(text="Cadastrar Aula", content=aula_tab),
             ft.Tab(text="Progresso do Aluno", content=progresso_tab),
             ft.Tab(text="Atualizar Aluno", content=atualizar_tab),
         ]
     )

     page.add(
		 tabs
	 )
    
ft.app(main)
    
if __name__ == "__main__": 
     # gera a interface
     ft.app(target=main)