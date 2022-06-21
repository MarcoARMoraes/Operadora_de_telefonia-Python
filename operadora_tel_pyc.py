from tkinter import  *
import phonenumbers

menu_inicial = Tk()
menu_inicial.title('Descubra a operadora de telefonia')
menu_inicial.geometry("400x180")
menu_inicial.resizable(False, False)

#def cmd_Click():
    #print('Olá, mundo!')

def encontra_numero():
    telefone = str(textbox1.get())
    telefone_ajustado = phonenumbers.parse(telefone)
    from phonenumbers import geocoder
    local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
    #label2['text'] = local
    telefone_formulario = (telefone.format(telefone))
    telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")
    telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,
                                                    phonenumbers.PhoneNumberFormat.NATIONAL)
    from phonenumbers import carrier
    operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
    label2['text'] = (f'{local}, \n {telefone_formatado}, \n {operadora}')
    #print(numero_para_encontrar)

#label
label1 = Label(text="Digite o número da linha com DDD e o código nacional +55: ", font="Arial 10 bold")
label1.grid()

#entrada do usuário
textbox1 = Entry(menu_inicial)
textbox1.focus()
textbox1.grid()

#botão
cmd = Button(menu_inicial, text="Executar", command=encontra_numero)
cmd.grid()

label2 = Label(menu_inicial, text="", width=10, height=5, relief='groove', padx=100, font="Arial 10 bold")
label2.place(x=315, y=350)
label2.grid()

label3 = Label(text="Desenvolvido por Marco Moraes", font="Arial 9 italic")
label3.grid()

menu_inicial.mainloop()