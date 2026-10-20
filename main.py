import flet as ft




def main(page: ft.Page):
    # variaveis simples e compostas e textos
    emprestimos = []
    resultado = ft.Text('')
    largura = 350



    # função dos botoes 
    def limpar(e):
        usuario.value = ''
        qtd.value = ''
        equipamento.value = None
        resultado.value = ''
        page.update()
   

    
 
    def solicitar(e):
        if usuario.value == '':
            resultado.value = 'Informe o nome do responsável.'
            page.update()
            return 
        if qtd.value == '' or  qtd.value < 0:
            resultado.value = 'Digite uma quantidade inteira válida.'
            page.update()
            return
        if equipamento.value is None:
            resultado.value = 'Selecione um equipamento.'
            page.update()
            return

        emprestimo = {
            "responsavel": resultado.value,
            "equipamento": qtd.value,
            "quantidade": equipamento.value
        }


        emprestimos.append(emprestimo) 

    # botoes 
    botao_limpar = ft.Button(
        content='Limpar',
        on_click=limpar
    )

    botao_solicitar = ft.Button(
        content='solicitar emprestimo',
        on_click=solicitar
    )


    
    # objetos 

    usuario = ft.TextField(
        label='Digite seu nome:',
        width=largura
    )


    qtd = ft.TextField(
        label='Digite a quantidade',
        width=largura
    )

    equipamento = ft.Dropdown(
        label='Escolha o equipamento:',
        options=[
            ft.DropdownOption(key='notebook'),
            ft.DropdownOption(key='projetor'),
            ft.DropdownOption(key='multímetro')
        ],
        width=largura
    )

    # organizar elementos e adicionar na pagina 
   
    coluna = ft.Column(
        [
            usuario,equipamento,qtd,
ft.Row(
[botao_solicitar,botao_limpar],
alignment=ft.MainAxisAlignment.CENTER
)
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )


    page.add(coluna)




ft.run(main)



