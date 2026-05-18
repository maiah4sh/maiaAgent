"""
Guia Rápido de Início - Interface Gráfica do Agente Gemini
"""

import os
import sys

def print_header():
    """Imprime o cabeçalho."""
    print("=" * 60)
    print("🤖 AGENTE IA COM GEMINI - GUIA RÁPIDO")
    print("=" * 60)
    print()

def check_environment():
    """Verifica o ambiente."""
    print("✓ Verificando ambiente...\n")
    
    # Python version
    print(f"✓ Python: {sys.version.split()[0]}")
    
    # API Key
    if os.getenv("GEMINI_API_KEY"):
        print("✓ Chave API: Configurada ✅")
    else:
        print("✗ Chave API: Não configurada ❌")
        print("\n  Para configurar, execute:")
        print("  $env:GEMINI_API_KEY = 'sua-chave-aqui'")
        print("\n  Obtenha em: https://aistudio.google.com/app/apikey\n")
    
    # Dependencies
    deps = {
        'google.generativeai': 'Google Generative AI',
        'tkinter': 'Interface Gráfica'
    }
    
    print("\n✓ Verificando dependências:\n")
    for module, name in deps.items():
        try:
            __import__(module)
            print(f"  ✓ {name}")
        except ImportError:
            print(f"  ✗ {name}")

def show_quick_start():
    """Mostra guia rápido."""
    print("\n" + "=" * 60)
    print("INÍCIO RÁPIDO")
    print("=" * 60)
    print("""
1️⃣  Instale as dependências (primeira vez):
    pip install -r requirements.txt

2️⃣  Configure sua chave API:
    $env:GEMINI_API_KEY = 'sua-chave-aqui'

3️⃣  Inicie a interface gráfica:
    python run_gui.py

4️⃣  Use o agente:
    - 💬 Chat: Converse em tempo real
    - 📋 Tarefas: Execute tarefas específicas
    - 📚 Histórico: Veja conversas salvas
    - 💾 Salve suas conversas

""")

def show_features():
    """Mostra funcionalidades."""
    print("=" * 60)
    print("FUNCIONALIDADES DISPONÍVEIS")
    print("=" * 60)
    print("""
📋 TAREFAS DISPONÍVEIS:

1. Processar Tarefa
   └─ Execute qualquer tarefa que desejar

2. Analisar Texto
   └─ Análise detalhada de sentimento, temas, estrutura

3. Gerar Ideias
   └─ Crie ideias criativas sobre um tópico

4. Resolver Problema
   └─ Encontre soluções com IA avançada

💬 CHAT INTERATIVO:
   └─ Converse naturalmente com o agente
   └─ Histórico com timestamps
   └─ Salvamento de conversas

📚 HISTÓRICO DE CONVERSAS:
   └─ Veja todas as conversas salvas
   └─ Carregue sessões anteriores
   └─ Gerencie suas conversas
""")

def show_python_examples():
    """Mostra exemplos em Python."""
    print("=" * 60)
    print("EXEMPLOS EM PYTHON")
    print("=" * 60)
    print("""
from gemini_agent import GeminiAgent

# Inicializar
agent = GeminiAgent()

# Chat simples
response = agent.chat("Como você funciona?")

# Processar tarefa
result = agent.process_task("Escreva um poema")

# Analisar texto
analysis = agent.analyze_text("Seu texto...")

# Gerar ideias
ideas = agent.generate_ideas("Tema interessante", num_ideas=5)

# Resolver problema
solution = agent.solve_problem("Meu problema é...")

# Visualizar histórico
history = agent.get_conversation_history()

# Limpar histórico
agent.clear_history()

# Personalizar prompt
agent.set_system_prompt("Novo prompt customizado")
""")

def show_troubleshooting():
    """Mostra troubleshooting."""
    print("\n" + "=" * 60)
    print("SOLUÇÃO DE PROBLEMAS")
    print("=" * 60)
    print("""
❌ "Chave da API não encontrada"
✓ Configure: $env:GEMINI_API_KEY = 'sua-chave'
✓ Ou crie arquivo .env com a chave
✓ Reinicie o terminal

❌ "Interface não abre"
✓ Verifique Tkinter: python -m tkinter
✓ Em Linux: sudo apt-get install python3-tk
✓ Verifique a chave API

❌ "ModuleNotFoundError"
✓ Instale: pip install -r requirements.txt

❌ "Rate limit exceeded"
✓ Aguarde alguns minutos
✓ Considere plano pago do Gemini

❌ "Interface lenta"
✓ Normal durante processamento IA
✓ Não feche a janela
✓ Aguarde a resposta
""")

def show_tips():
    """Mostra dicas úteis."""
    print("\n" + "=" * 60)
    print("💡 DICAS ÚTEIS")
    print("=" * 60)
    print("""
1. Use prompts específicos e bem estruturados
2. Mantenha contexto dentro da mesma conversa
3. Salve conversas importantes regularmente
4. Limpe histórico se ficar lento
5. Use "Resolver Problema" com contexto detalhado
6. Para tarefas complexas, divida em partes
7. Crie um .env para não expor a chave

""")

def main():
    """Função principal."""
    print_header()
    check_environment()
    show_quick_start()
    show_features()
    show_python_examples()
    show_troubleshooting()
    show_tips()
    
    print("=" * 60)
    print("Pronto para começar? Execute: python run_gui.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
