"""
Exemplo de uso do Agente IA Gemini
Este script demonstra como usar o agente em uma aplicação simples.
"""

from gemini_agent import GeminiAgent


def main():
    """Exemplo principal de uso do agente."""
    
    # Inicializa o agente Gemini
    print("Iniciando Agente IA Gemini...")
    print("-" * 50)
    
    try:
        agent = GeminiAgent()
    except ValueError as e:
        print(f"Erro: {e}")
        print("\nConfigure a chave API antes de continuar!")
        return
    
    # Exemplo 1: Conversa simples
    print("\n📝 Exemplo 1: Conversa Simples")
    print("-" * 50)
    
    response = agent.chat("Olá! Como você pode me ajudar?")
    print(f"Resposta: {response[:200]}...\n")
    
    # Exemplo 2: Tarefa específica
    print("📝 Exemplo 2: Processamento de Tarefa")
    print("-" * 50)
    
    task = "Crie uma lista com 5 dicas de produtividade"
    result = agent.process_task(task)
    print(f"Tarefa: {task}")
    print(f"Resultado:\n{result}\n")
    
    # Exemplo 3: Geração de ideias
    print("💡 Exemplo 3: Geração de Ideias")
    print("-" * 50)
    
    ideas = agent.generate_ideas("tecnologias para aprender em 2026", num_ideas=5)
    print(f"Ideias geradas:\n{ideas}\n")
    
    # Exemplo 4: Resolver problema
    print("🔧 Exemplo 4: Resolução de Problema")
    print("-" * 50)
    
    problem = "Preciso estruturar meu projeto Python. Qual é a melhor estrutura de pastas?"
    solution = agent.solve_problem(problem)
    print(f"Problema: {problem}")
    print(f"Solução:\n{solution}\n")


if __name__ == "__main__":
    main()
