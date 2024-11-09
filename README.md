# Calculadora com Interface Gráfica em Python

Este é um projeto de uma calculadora com interface gráfica desenvolvida em Python utilizando a biblioteca Tkinter. O projeto é modularizado em diferentes arquivos, incluindo tratamento de entrada, exibição de interface e lógica de cálculo. A calculadora suporta operações matemáticas básicas e algumas funcionalidades avançadas.

## Estrutura do Projeto

- `main.py:` Arquivo principal que inicializa a interface e conecta as funções de cálculo aos botões da interface.
- `calculadora_interface_grafica.py:` Define a classe `Calculadora_Interface_Grafica`, responsável por configurar e gerenciar a interface gráfica e as interações do usuário.
- `calculadorafatorial.py:` Contém as funções de construção dos elementos gráficos, como janela, display e botões.
- `calculadoratratamento.py:` Contém as funções de tratamento e validação das expressões matemáticas, como limpeza de caracteres inválidos, resolução de operações de potência e processamento de expressões com parênteses.

## Funcionalidades

- **Operações Básicas:** Suporta adição, subtração, multiplicação e divisão.
- **Potenciação:** Permite realizar cálculos com expoentes.
- **Parênteses:** Suporta expressões matemáticas com parênteses.
- **Interface Amigável:** Utiliza o Tkinter para criar uma interface gráfica intuitiva, com botões coloridos e organizados para melhor usabilidade.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/nome_do_repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd nome_do_repositorio
```
3. Certifique-se de que você tem o Python instalado. Este projeto requer Python 3.6 ou superior.

## Como Executar

1. Execute o arquivo principal main.py:

```bash
python main.py
```

2. A calculadora será exibida em uma nova janela. Utilize os botões para realizar cálculos.

## Arquivos e Funções Principais

`calculadora_interface_grafica.py`

Define a classe `Calculadora_Interface_Grafica`, que gerencia:

- Configuração dos botões e display.
- Adição de texto ao display e tratamento de eventos de cálculo (Enter e =, por exemplo).
- Tratamento de erros e exibição de mensagens de erro para entradas inválidas.

`calculadorafatorial.py`
 
Funções para construção da interface gráfica:

- `fazer_janela():` Cria a janela principal da calculadora.
- `fazer_label():` Cria o rótulo para exibir mensagens e resultados.
- `fazer_display():` Configura a área de exibição de entradas e resultados.
- `fazer_button():` Configura os botões da calculadora com estilo e funcionalidade.
- `fazer_buttons():` Organiza os botões em uma grade.

`calculadoratratamento.py`

Funções para tratamento e resolução de expressões matemáticas:
- `del_invalid_chars():` Remove caracteres não numéricos ou operadores inválidos
- `solve_exponentiations():` Resolve operações de potência na expressão.
- `resolve_parenteses():` Resolve operações dentro de parênteses.
- `calcular():` Avalia a expressão final e retorna o resultado.

## Exemplo de Uso

1. Insira uma expressão matemática, como `2+3*5`.
2. Clique no botão `=` ou pressione `Enter` para calcular.
3. O resultado aparecerá no display da calculadora.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests com melhorias ou correções.

## Licença

Este projeto é licenciado sob a Licença MIT.