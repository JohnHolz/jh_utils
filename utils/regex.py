"""
# Arquivos:
- Capturar arquivos .png: .*png
- Capturar arquivos .csv: .*csv

# Documentos Brasileiros:
- CPF: \d{3}\.?\d{3}\.?\d{3}[-.]?\d{2}
    - Formatos: 000.000.000-00
                00000000000
                000.000.000.00

- CNPJ: \d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}
    - Formato: 00.000.000/0000-00

- Placa de veiculo (Padrão Antigo): [A-Z]+-\d{4}
    - Formato: AAA-0000

- Placa de veículo (Padrão Novo):
    - Formato: 

# Telefones:
- Telefone Celular e Fixo Brasil: \([0-9]{2}\).([1-9]{4,5}-[0-9]{4})
    - Formato: (00) 00000-0000

- Telefone com DDI:
    - Formato:

# Geolozalização
- CEP: \d{5}-\d{3}
    - Formato: 00000-000

# Tecnologia:
- IP: \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}
    - Formatos: 000.0.000.00
                000.000.00.000
                000.000.0.00

# Data e Hora:
- Data: [1-3]?\d\s+de\s+[A-Z][a-zç]{3,8}\s+de\s+[12]\d{3}
    - Formato: 01 de Maio de 1993

- Data: Data:[\s]?[0-9]{2}[-/:][0-9]{2}[-/:][0-9]{2,4}
    - Formato: Data:00/00/0000
               Data: 00/00/0000
               Data:00-00-0000
               Data: 00-00-0000
               Data:00:00:0000
               Data: 00:00:0000

- Hora: \d{2}h\d{2}min\d{2}s
    - Formato: 00h00min00s

# Custom:
- Custom 1: [a-zA-Z]\w{0,9}
    - String de no máximo 10 caracteres sendo o primeiro uma letra, sem caracteres especiais.

"""

cnpj = '\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'
cpf = '\d{3}\.?\d{3}\.?\d{3}[-.]?\d{2}'
time = '\d{2}h\d{2}min\d{2}s'
data = '[\s]?[0-9]{2}[-/:][0-9]{2}[-/:][0-9]{2,4}'
datetime = '[1-3]?\d\s+de\s+[A-Z][a-zç]{3,8}\s+de\s+[12]\d{3}'
ip = '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
phone = '\([0-9]{2}\).([1-9]{4,5}-[0-9]{4})'
numbers = '^([\s\d]+)$'
remove_special_characters = '[^A-Za-z0-9]+'
