import sys

DATABASE_PATH = "Gestor de clientes/gestor/clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = 'Gestor de Clientes/gestor/tests/clientes_test.csv'