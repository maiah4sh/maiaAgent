# 🤖 Agente IA com Gemini

Um agente inteligente autônomo que utiliza a **API Gemini do Google** para processar e responder a solicitações.

## 🚀 Funcionalidades

- **Chat Interativo**: Conversa contínua com histórico
- **Processamento de Tarefas**: Execute tarefas específicas usando IA
- **Análise de Texto**: Análise detalhada de conteúdo
- **Geração de Ideias**: Crie ideias criativas sobre qualquer tópico
- **Resolução de Problemas**: Encontre soluções com IA
- **Histórico de Conversa**: Mantenha contexto ao longo da sessão
- **System Prompt Customizável**: Personalize o comportamento do agente

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Chave de API do Gemini (gratuita em https://aistudio.google.com/app/apikey)
- Tkinter (incluído no Python por padrão)

## 🔧 Instalação Rápida

### 1. Clone ou baixe o projeto

```bash
cd seu-diretorio-do-projeto
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a Chave API

#### Opção A: Variável de Ambiente (Recomendado)
```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY = "sua-chave-aqui"

# Windows (CMD)
set GEMINI_API_KEY=sua-chave-aqui

# Linux/Mac
export GEMINI_API_KEY="sua-chave-aqui"
```

#### Opção B: Arquivo .env
Crie um arquivo `.env` no diretório do projeto:
```
GEMINI_API_KEY=sua-chave-aqui
```

## 📖 Como Usar

### 🖥️ Interface Gráfica (Recomendado)

A forma mais fácil e intuitiva de usar o agente:

```bash
python run_gui.py
```

**Recursos da interface:**
- 💬 **Chat**: Converse com o agente em tempo real
- 📋 **Tarefas**: Execute tarefas específicas (análise, geração de ideias, etc.)
- 📚 **Histórico**: Visualize e carregue conversas salvas
- 💾 **Salvamento**: Guarde suas conversas automaticamente

### 📝 Exemplos em Python

#### Exemplo 1: Chat Interativo

```python
from gemini_agent import GeminiAgent

agent = GeminiAgent()

# Conversa com o agente
response = agent.chat("Olá, como você pode me ajudar?")
print(response)
```

#### Exemplo 2: Processar Tarefa

```python
# Processa uma tarefa específica
result = agent.process_task("Escreva um poema sobre IA")
print(result)
```

#### Exemplo 3: Análise de Texto

```python
# Analisa um texto
text = "Seu texto aqui..."
analysis = agent.analyze_text(text)
print(analysis)
```

#### Exemplo 4: Gerar Ideias

```python
# Gera ideias sobre um tópico
ideas = agent.generate_ideas("startups de tecnologia", num_ideas=5)
print(ideas)
```

#### Exemplo 5: Resolver Problema

```python
# Resolve um problema
problem = "Como estruturar um projeto Python?"
solution = agent.solve_problem(problem)
print(solution)
```

## 🎯 Executar Aplicação

```bash
# Interface gráfica (recomendado)
python run_gui.py

# Chat interativo em terminal
python hello.py

# Acesso direto ao agente
python gemini_agent.py
```

### Interface Gráfica - Features

#### Aba 1: 💬 Chat
- Conversa em tempo real com o agente
- Histórico colorido e formatado
- Timestamps automáticos
- Salve suas conversas com um clique

#### Aba 2: 📋 Tarefas
- Selecione o tipo de tarefa
- Processe tarefas específicas:
  - Processar Tarefa
  - Analisar Texto
  - Gerar Ideias
  - Resolver Problema
- Copie resultados facilmente

#### Aba 3: 📚 Histórico
- Veja todas as conversas salvas
- Visualize conversas anteriores
- Recarregue sessões antigas
- Organize suas discussões

## 📚 Métodos Disponíveis

### `__init__(api_key, model)`
Inicializa o agente com configurações personalizadas.

### `chat(user_message)`
Mantém conversa com histórico.

### `process_task(task, context)`
Processa uma tarefa com contexto opcional.

### `analyze_text(text)`
Analisa detalhadamente um texto.

### `generate_ideas(topic, num_ideas)`
Gera ideias criativas sobre um tópico.

### `solve_problem(problem, constraints)`
Resolve um problema com restrições opcionais.

### `get_conversation_history()`
Retorna o histórico completo da conversa.

### `clear_history()`
Limpa o histórico da conversa.

### `set_system_prompt(new_prompt)`
Personaliza o comportamento do agente.

## 🔑 Obter Chave API

1. Acesse: https://aistudio.google.com/app/apikey
2. Clique em "Create API Key"
3. Copie a chave gerada
4. Configure conforme instruções acima

## ⚙️ Configurações Avançadas

### Mudar Modelo

```python
agent = GeminiAgent(model="gemini-1.5-pro")
```

### Personalizar Comportamento

```python
agent.set_system_prompt(
    "Você é um especialista em Python com 20 anos de experiência."
)
```

## 📝 Notas Importantes

- A API Gemini oferece 15 requisições por minuto no plano gratuito
- Cada conversa mantém histórico apenas na sessão atual
- Use `clear_history()` para limpar o contexto de conversa
- Modelos disponíveis: `gemini-2.0-flash`, `gemini-1.5-pro`, `gemini-1.5-flash`

## 🐛 Troubleshooting

### "Chave da API Gemini não encontrada"
- Verifique se a variável de ambiente está configurada corretamente
- Ou crie um arquivo `.env` com a chave
- Reinicie o terminal após configurar a variável

### "Rate limit exceeded"
- Aguarde alguns minutos antes de fazer novas requisições
- Considere usar o plano pago do Gemini

### "Modelo não encontrado"
- Verifique se o nome do modelo está correto
- Consulte a documentação do Gemini para modelos disponíveis

### Interface gráfica não abre
- Verifique se o Tkinter está instalado: `python -m tkinter`
- Em Linux, pode ser necessário instalar: `sudo apt-get install python3-tk`
- Verifique se a chave API está configurada

### "ModuleNotFoundError: No module named 'google.generativeai'"
```bash
pip install google-generativeai
```

## 🎨 Interface Gráfica - Temas

A interface inclui:
- 🎨 **Tema escuro profissional** para melhor legibilidade
- ⚡ **Processamento assíncrono** - não congela ao usar IA
- 💾 **Salvamento automático** de conversas
- 📊 **Histórico organizado** em JSON

## 🚀 Dicas de Uso

### Para melhor performance:
1. Use prompts específicos e bem estruturados
2. Mantenha o contexto das conversas dentro de uma sessão
3. Limpe o histórico periodicamente para melhor performance
4. Use a função "Resolver Problema" com contexto detalhado

### Salvando conversas:
```bash
# Conversas salvas em:
./conversas_salvas/conversa_YYYYMMDD_HHMMSS.json

# Carregue diretamente na interface ou
# Processe com Python:
import json
with open('conversas_salvas/seu_arquivo.json') as f:
    history = json.load(f)
```

## 📱 Atalhos Úteis (GUI)

| Ação | Tecla |
|------|-------|
| Enviar mensagem | `Ctrl+Enter` (em desenvolvimento) |
| Limpar chat | Botão de interface |
| Salvar conversa | Botão de interface |
| Copiar resultado | Botão de interface |

## 🔌 Personalização Avançada

### Mudar modelo:
```python
agent = GeminiAgent(model="gemini-1.5-pro")
```

### Personalizar prompt do sistema:
```python
custom_prompt = """
Você é um especialista em Python com 20 anos de experiência.
Responda sempre com exemplos de código práticos.
"""
agent.set_system_prompt(custom_prompt)
```

### Usar em scripts:
```python
from gemini_agent import GeminiAgent
import json

agent = GeminiAgent()

# Processe múltiplas tarefas
tasks = [
    "Tarefa 1",
    "Tarefa 2",
    "Tarefa 3"
]

results = []
for task in tasks:
    result = agent.process_task(task)
    results.append(result)

# Salve resultados
with open('resultados.json', 'w') as f:
    json.dump(results, f)
```

## 📊 Estatísticas

- ⚙️ **3 modos de operação**: GUI, CLI, API
- 🧠 **5 funções principais**: Chat, Tarefas, Análise, Ideias, Problemas
- 📁 **3 tipos de interação**: Chat, Processamento, Histórico
- 🔄 **Histórico persistente**: JSON

## ✨ Features Exclusivas

✅ Interface gráfica intuitiva com Tkinter
✅ Chat com histórico formatado e colorido  
✅ Múltiplos tipos de tarefas
✅ Salvamento automático de conversas
✅ Processamento assíncrono (não congela UI)
✅ Suporte a modelos Gemini
✅ Sistema de prompt customizável
✅ Histórico de conversas em JSON

## 🐛 Troubleshooting

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para melhorar o código e adicionar novas funcionalidades.

---

**Desenvolvido com ❤️ usando Gemini AI**
