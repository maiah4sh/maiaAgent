"""
Inicializador da Interface Gráfica
Execute este arquivo para abrir a interface visual do Agente Gemini.
"""

import os
import sys
from pathlib import Path

# Verifica se está no diretório correto
if not Path("gemini_agent.py").exists():
    print("❌ Erro: Execute este script no diretório do projeto")
    sys.exit(1)

# Verifica variável de ambiente
if not os.getenv("GEMINI_API_KEY"):
    print("⚠️  Aviso: GEMINI_API_KEY não configurada")
    print("Configure a chave antes de usar a interface:")
    print("  $env:GEMINI_API_KEY = 'sua-chave-aqui'")
    print("\nDeseja continuar mesmo assim? (A interface abrirá, mas o agente não funcionará)")
    response = input("Digite 's' para continuar ou qualquer outra tecla para cancelar: ")
    if response.lower() != 's':
        print("Cancelado.")
        sys.exit(0)

print("Iniciando interface gráfica...")
print("Aguarde enquanto o agente é carregado...\n")

try:
    from gui import main
    main()
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("\nCertifique-se de que todas as dependências estão instaladas:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro ao iniciar: {e}")
    sys.exit(1)
