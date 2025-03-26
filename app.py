from GUI import Calculadora_Interface_Grafica
from fatorial import fazer_janela, fazer_display, fazer_label,fazer_buttons
from tratamento import calcular

def main():
    janela = fazer_janela()
    display = fazer_display(janela, row=1, column=0, columnspan=5, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = fazer_label(janela, row=0, column=0, columnspan=5, sticky='news')
    buttons = fazer_buttons(janela, starting_row=2)

    GUI = Calculadora_Interface_Grafica(janela, label, display, buttons, calcular)
    GUI.start_interface_grafica()

if __name__ == '__main__':
    main()
