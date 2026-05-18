"""
Exemplos Avançados de Uso do Agente Gemini
Demonstra funcionalidades mais complexas e casos de uso reais.
"""

from gemini_agent import GeminiAgent
import json
from datetime import datetime
from pathlib import Path


class AdvancedExamples:
    """Exemplos avançados de uso."""
    
    def __init__(self):
        """Inicializa os exemplos."""
        self.agent = GeminiAgent()
        self.results = []
    
    def exemplo_1_conversa_multilinear(self):
        """
        Exemplo 1: Conversa com contexto progressivo.
        Mostra como o agente mantém contexto ao longo da conversa.
        """
        print("\n" + "="*60)
        print("EXEMPLO 1: Conversa com Contexto Progressivo")
        print("="*60)
        
        messages = [
            "Explique o conceito de machine learning em uma frase",
            "Agora dê um exemplo prático",
            "Como isso se aplica em IA?",
            "Que linguagem de programação é melhor?"
        ]
        
        for msg in messages:
            print(f"\nVocê: {msg}")
            response = self.agent.chat(msg)
            print(f"Agente: {response[:150]}...\n")
    
    def exemplo_2_batch_processing(self):
        """
        Exemplo 2: Processar múltiplas tarefas em lote.
        Útil para processar listas de tarefas.
        """
        print("\n" + "="*60)
        print("EXEMPLO 2: Processamento em Lote")
        print("="*60)
        
        tarefas = [
            "Crie um algoritmo de busca binária",
            "Explique expressões regulares",
            "O que é programação funcional?"
        ]
        
        resultados = {}
        
        for i, tarefa in enumerate(tarefas, 1):
            print(f"\n[{i}/{len(tarefas)}] Processando: {tarefa[:50]}...")
            resultado = self.agent.process_task(tarefa)
            resultados[tarefa] = resultado
        
        # Salvar resultados
        filename = f"batch_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)
        
        print(f"\n✓ Resultados salvos em: {filename}")
    
    def exemplo_3_analise_textos_multiplos(self):
        """
        Exemplo 3: Analisar múltiplos textos.
        Demonstra análise em massa.
        """
        print("\n" + "="*60)
        print("EXEMPLO 3: Análise de Textos Múltiplos")
        print("="*60)
        
        textos = [
            "Python é incrível para ciência de dados!",
            "Não gosto de bugs no código.",
            "JavaScript é versátil e onipresente."
        ]
        
        analises = {}
        
        for i, texto in enumerate(textos, 1):
            print(f"\n[{i}/{len(textos)}] Analisando: {texto}")
            analise = self.agent.analyze_text(texto)
            analises[texto] = analise
        
        # Exibir resumo
        print("\n" + "-"*60)
        print("RESUMO DAS ANÁLISES:")
        for texto, analise in analises.items():
            print(f"\nTexto: {texto}")
            print(f"Análise: {analise[:200]}...")
    
    def exemplo_4_contexto_com_restricoes(self):
        """
        Exemplo 4: Resolver problema com contexto e restrições.
        Mostra uso de contexto e restrições juntas.
        """
        print("\n" + "="*60)
        print("EXEMPLO 4: Resolver com Contexto e Restrições")
        print("="*60)
        
        problema = "Preciso estruturar um projeto de IA"
        
        contexto = """
        - Projeto iniciante em Python
        - Precisa ser escalável
        - Orçamento limitado
        - Prazo de 2 meses
        """
        
        restricoes = """
        - Máximo 5 tecnologias principais
        - Código deve ser documentado
        - Sem dependências pesadas
        """
        
        print(f"Problema: {problema}")
        print(f"Contexto: {contexto}")
        print(f"Restrições: {restricoes}")
        
        prompt_completo = f"""
{problema}

Contexto:
{contexto}

Restrições:
{restricoes}

Por favor, forneça uma solução estruturada e prática.
        """
        
        solucao = self.agent.process_task(prompt_completo)
        
        print(f"\nSolução:\n{solucao}")
    
    def exemplo_5_gerador_ideias_tematico(self):
        """
        Exemplo 5: Gerar ideias de forma temática.
        Demonstra geração criativa com múltiplos temas.
        """
        print("\n" + "="*60)
        print("EXEMPLO 5: Gerador de Ideias Temático")
        print("="*60)
        
        temas = {
            "Startups": 5,
            "Projetos Python": 4,
            "Apps Inovadores": 6
        }
        
        todas_ideias = {}
        
        for tema, num_ideias in temas.items():
            print(f"\n📝 Gerando {num_ideias} ideias sobre: {tema}")
            ideias = self.agent.generate_ideas(tema, num_ideias)
            todas_ideias[tema] = ideias
        
        # Salvar ideias
        filename = f"ideias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(todas_ideias, f, ensure_ascii=False, indent=2)
        
        print(f"\n✓ Ideias salvas em: {filename}")
    
    def exemplo_6_sistema_prompt_customizado(self):
        """
        Exemplo 6: Usar prompt customizado.
        Mostra como personalizar o comportamento do agente.
        """
        print("\n" + "="*60)
        print("EXEMPLO 6: Prompt do Sistema Customizado")
        print("="*60)
        
        # Criar novo agente com prompt customizado
        agente_especialista = GeminiAgent()
        
        novo_prompt = """
Você é um especialista em Python com 15 anos de experiência.
Suas respostas devem:
1. Incluir exemplos de código práticos
2. Explicar conceitos de forma técnica
3. Mencionar boas práticas e padrões
4. Alertar sobre armadilhas comuns
5. Sugerir otimizações quando aplicável
        """
        
        agente_especialista.set_system_prompt(novo_prompt)
        
        pergunta = "Como otimizar um loop em Python?"
        print(f"\nPergunta: {pergunta}")
        
        resposta = agente_especialista.chat(pergunta)
        print(f"\nResposta (especialista):\n{resposta}")
    
    def exemplo_7_salvar_carregar_historico(self):
        """
        Exemplo 7: Gerenciar histórico de conversas.
        Mostra como salvar e carregar conversas.
        """
        print("\n" + "="*60)
        print("EXEMPLO 7: Histórico de Conversas")
        print("="*60)
        
        # Realizar conversa
        print("\nRealizando conversa...")
        self.agent.chat("Olá! Como você funciona?")
        self.agent.chat("Pode dar um exemplo de uso?")
        self.agent.chat("Muito bom! Obrigado.")
        
        # Obter histórico
        historico = self.agent.get_conversation_history()
        
        # Salvar
        filename = f"historico_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(historico, f, ensure_ascii=False, indent=2)
        
        print(f"\n✓ Histórico salvo em: {filename}")
        print(f"Total de mensagens: {len(historico)}")
        
        # Exibir resumo
        print("\nResumo da conversa:")
        for i, msg in enumerate(historico, 1):
            role = msg['role'].upper()
            content = msg['content'][:60]
            print(f"  {i}. {role}: {content}...")
    
    def exemplo_8_processamento_texto_avancado(self):
        """
        Exemplo 8: Análise avançada de texto.
        Demonstra análise profunda de conteúdo.
        """
        print("\n" + "="*60)
        print("EXEMPLO 8: Análise Avançada de Texto")
        print("="*60)
        
        texto_complexo = """
Python é uma linguagem de programação de alto nível, interpretada,
com tipagem dinâmica e multiparadigma. Foi criada por Guido van Rossum
em 1991. É amplamente utilizada em ciência de dados, web e automação.
Sua comunidade é ativa e oferece milhares de bibliotecas.
        """
        
        prompt_analise = f"""
Analise o seguinte texto sob vários aspectos:

TEXTO:
{texto_complexo}

POR FAVOR ANALISE:
1. Estrutura gramatical
2. Complexidade do conteúdo
3. Tópicos principais
4. Sentimento geral
5. Audiência-alvo
6. Sugestões de melhoria
        """
        
        analise_detalhada = self.agent.process_task(prompt_analise)
        print(f"Análise Detalhada:\n{analise_detalhada}")


def main():
    """Executa todos os exemplos."""
    print("🚀 EXEMPLOS AVANÇADOS DO AGENTE GEMINI")
    print("="*60)
    
    try:
        exemplos = AdvancedExamples()
        
        # Escolher qual exemplo executar
        print("\nQual exemplo deseja executar?")
        print("1. Conversa com Contexto Progressivo")
        print("2. Processamento em Lote")
        print("3. Análise de Textos Múltiplos")
        print("4. Resolver com Contexto e Restrições")
        print("5. Gerador de Ideias Temático")
        print("6. Prompt Customizado")
        print("7. Histórico de Conversas")
        print("8. Análise Avançada de Texto")
        print("0. Executar Todos")
        
        escolha = input("\nDigite o número: ").strip()
        
        if escolha == "1":
            exemplos.exemplo_1_conversa_multilinear()
        elif escolha == "2":
            exemplos.exemplo_2_batch_processing()
        elif escolha == "3":
            exemplos.exemplo_3_analise_textos_multiplos()
        elif escolha == "4":
            exemplos.exemplo_4_contexto_com_restricoes()
        elif escolha == "5":
            exemplos.exemplo_5_gerador_ideias_tematico()
        elif escolha == "6":
            exemplos.exemplo_6_sistema_prompt_customizado()
        elif escolha == "7":
            exemplos.exemplo_7_salvar_carregar_historico()
        elif escolha == "8":
            exemplos.exemplo_8_processamento_texto_avancado()
        elif escolha == "0":
            print("\n⚠️ Executando TODOS os exemplos (pode demorar)...")
            exemplos.exemplo_1_conversa_multilinear()
            exemplos.exemplo_2_batch_processing()
            exemplos.exemplo_3_analise_textos_multiplos()
            exemplos.exemplo_4_contexto_com_restricoes()
            exemplos.exemplo_5_gerador_ideias_tematico()
            exemplos.exemplo_6_sistema_prompt_customizado()
            exemplos.exemplo_7_salvar_carregar_historico()
            exemplos.exemplo_8_processamento_texto_avancado()
        else:
            print("Opção inválida!")
        
        print("\n" + "="*60)
        print("✓ Exemplos concluídos!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\nCancelado pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    main()
