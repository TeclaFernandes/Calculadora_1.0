import tkinter as tk
from typing import List, Callable

class Calculadora_Interface_Grafica:

    def __init__(
        self,
        janela: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        button_list: List[List[tk.Button]],
        do_calcular: Callable[[str], str]
    ) -> None:
        self.janela = janela
        self.label = label
        self.display = display
        self.button_list = button_list
        self.do_calcular = do_calcular

    def start_interface_grafica(self) -> None:
        self._config_display()
        self._config_buttons()
        self.janela.mainloop()

    def _config_display(self) -> None:
        display = self.display
        display.bind('<Return>', self.do_calcular)
        display.bind('<KP_Enter>', self.do_calcular)

    def _config_buttons(self) -> None:
        buttons_list = self.button_list
        for row in buttons_list:
            for button in row:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear_display)
                    button.config(bg='#5ccda7', fg='#000')

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calcular)
                    button.config(bg='#009d71', fg='#000')

    def calcular(self, event=None) -> None:
        equacao = self.display.get()

        try:
            result = self.do_calcular(equacao)

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{equacao} = {result}')
        except OverflowError:
            self.label.config(text='Não foi possivel realizar essa conta, desculpa!')
        except Exception:
            self.label.config(text='Conta inválida')

    def add_text_to_display(self, event=None) -> None:
        self.display.insert('end', event.widget['text'])
        self.display.focus()

    def clear_display(self, event=None) -> None:
        self.display.delete(0, 'end')
