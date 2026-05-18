"""
Agente IA com Inteligência Artificial Gemini
Este módulo implementa um agente autônomo que utiliza a API Gemini do Google
para processar e responder a solicitações do usuário.
"""

import os
import re
import time
from typing import Optional, List
import google.generativeai as genai
from datetime import datetime

class GeminiAgent:
    """
    Agente IA que utiliza o modelo Gemini para processar tarefas e manter conversas.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-2.0-flash"):
        """
        Inicializa o agente Gemini.
        
        Args:
            api_key: Chave da API Gemini. Se None, procura em GEMINI_API_KEY
            model: Modelo Gemini a ser utilizado
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Chave da API Gemini não encontrada. "
                "Defina a variável de ambiente GEMINI_API_KEY"
            )
        
        genai.configure(api_key=self.api_key)
        self.model_name = model
        self.model = genai.GenerativeModel(model)
        self.conversation_history: List[dict] = []
        self.system_prompt = """Você é um assistente IA chamado AgentGemini. 
Seu objetivo é ajudar o usuário de forma precisa, educada e eficiente.
Responda em português brasileiro quando não indicado contrário."""
    
    def _generate_with_retry(self, prompt: str) -> str:
        """Gera conteúdo com retries em caso de quota/rate limit."""
        max_attempts = 3
        attempt = 0
        while attempt < max_attempts:
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                message = str(e)
                if "Quota exceeded" in message or "429" in message or "rate limit" in message.lower():
                    attempt += 1
                    retry_delay = 5
                    match = re.search(r"retry in (\d+(?:\.\d+)?)s", message, re.IGNORECASE)
                    if match:
                        retry_delay = float(match.group(1))
                    elif match := re.search(r"seconds: (\d+)", message, re.IGNORECASE):
                        retry_delay = float(match.group(1))
                    if attempt >= max_attempts:
                        return (
                            f"Erro de quota do Gemini após {attempt} tentativas: {message}. "
                            "Tente novamente mais tarde ou revise sua cota/plano."
                        )
                    time.sleep(retry_delay)
                    continue
                return f"Erro ao processar tarefa: {message}"
    
    def process_task(self, task: str, context: Optional[str] = None) -> str:
        """
        Processa uma tarefa usando o Gemini.
        
        Args:
            task: Tarefa a ser processada
            context: Contexto adicional (opcional)
        
        Returns:
            Resposta do modelo Gemini
        """
        prompt = task
        if context:
            prompt = f"Contexto: {context}\n\nTarefa: {task}"
        
        try:
            return self._generate_with_retry(prompt)
        except Exception as e:
            return f"Erro ao processar tarefa: {str(e)}"
    
    def chat(self, user_message: str) -> str:
        """
        Mantém uma conversa com histórico com o usuário.
        
        Args:
            user_message: Mensagem do usuário
        
        Returns:
            Resposta do agente
        """
        # Adiciona mensagem do usuário ao histórico
        self.conversation_history.append({
            "role": "user",
            "timestamp": datetime.now().isoformat(),
            "content": user_message
        })
        
        # Prepara o histórico para o modelo
        conversation_text = self.system_prompt + "\n\n"
        for msg in self.conversation_history:
            role = "Usuário" if msg["role"] == "user" else "Assistente"
            conversation_text += f"{role}: {msg['content']}\n"
        
        conversation_text += "Assistente:"
        
        try:
            assistant_message = self._generate_with_retry(conversation_text)
            
            # Adiciona resposta do assistente ao histórico
            self.conversation_history.append({
                "role": "assistant",
                "timestamp": datetime.now().isoformat(),
                "content": assistant_message
            })
            
            return assistant_message
        except Exception as e:
            return f"Erro na conversa: {str(e)}"
    
    def analyze_text(self, text: str) -> str:
        """
        Analisa um texto fornecido.
        
        Args:
            text: Texto a ser analisado
        
        Returns:
            Análise do texto
        """
        prompt = f"""Analise o seguinte texto de forma detalhada, considerando:
1. Sentimento/tom geral
2. Temas principais
3. Estrutura e clareza
4. Sugestões de melhoria

Texto: {text}"""
        
        return self.process_task(prompt)
    
    def generate_ideas(self, topic: str, num_ideas: int = 5) -> str:
        """
        Gera ideias sobre um tópico.
        
        Args:
            topic: Tópico para gerar ideias
            num_ideas: Número de ideias a gerar
        
        Returns:
            Lista de ideias geradas
        """
        prompt = f"Gere {num_ideas} ideias criativas e inovadoras sobre: {topic}"
        return self.process_task(prompt)
    
    def solve_problem(self, problem: str, constraints: Optional[str] = None) -> str:
        """
        Resolve um problema fornecido.
        
        Args:
            problem: Descrição do problema
            constraints: Restrições ou requisitos adicionais
        
        Returns:
            Solução proposta
        """
        prompt = f"Problema: {problem}"
        if constraints:
            prompt += f"\n\nRestrições: {constraints}"
        prompt += "\n\nPor favor, forneça uma solução detalhada."
        
        return self.process_task(prompt)
    
    def get_conversation_history(self) -> List[dict]:
        """
        Retorna o histórico de conversa.
        
        Returns:
            Lista com todo o histórico da conversa
        """
        return self.conversation_history.copy()
    
    def clear_history(self) -> None:
        """Limpa o histórico da conversa."""
        self.conversation_history.clear()
    
    def set_system_prompt(self, new_prompt: str) -> None:
        """
        Define um novo prompt do sistema.
        
        Args:
            new_prompt: Novo prompt do sistema
        """
        self.system_prompt = new_prompt


def main():
    """Função principal com exemplos de uso."""
    
    print("=" * 60)
    print("Agente IA com Gemini - Exemplos de Uso")
    print("=" * 60)
    
    # Inicializa o agente
    try:
        agent = GeminiAgent()
        print("✓ Agente inicializado com sucesso!\n")
    except ValueError as e:
        print(f"✗ Erro: {e}")
        print("\nInstruções:")
        print("1. Obtenha sua chave API em: https://aistudio.google.com/app/apikey")
        print("2. Defina a variável de ambiente: GEMINI_API_KEY=sua_chave_aqui")
        return
    
    # Exemplo 1: Chat interativo
    print("--- Exemplo 1: Chat Interativo ---")
    print("Digite 'sair' para encerrar o chat\n")
    
    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() == 'sair':
            break
        if not user_input:
            continue
        
        response = agent.chat(user_input)
        print(f"Agente: {response}\n")
    
    # Exemplo 2: Processar tarefa
    print("\n--- Exemplo 2: Processamento de Tarefa ---")
    task = "Explique o conceito de machine learning em 3 parágrafos"
    print(f"Tarefa: {task}")
    result = agent.process_task(task)
    print(f"Resultado:\n{result}\n")
    
    # Exemplo 3: Gerar ideias
    print("--- Exemplo 3: Geração de Ideias ---")
    topic = "aplicações práticas de IA no dia a dia"
    print(f"Tópico: {topic}")
    ideas = agent.generate_ideas(topic, 3)
    print(f"Ideias:\n{ideas}\n")
    
    # Exemplo 4: Resolver problema
    print("--- Exemplo 4: Resolução de Problema ---")
    problem = "Como otimizar a velocidade de um script Python lento?"
    print(f"Problema: {problem}")
    solution = agent.solve_problem(problem)
    print(f"Solução:\n{solution}\n")


if __name__ == "__main__":
    main()
