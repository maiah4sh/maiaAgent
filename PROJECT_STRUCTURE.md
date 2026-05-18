# 📁 Estrutura do Projeto - Agente IA Gemini

## 📊 Visão Geral da Estrutura

```
Python_molz1/
├── 🤖 Núcleo do Agente
│   ├── gemini_agent.py          (Classe principal do agente)
│   ├── gui.py                   (Interface gráfica Tkinter)
│   └── hello.py                 (Exemplo de uso)
│
├── 🚀 Inicializadores
│   ├── run_gui.py               (Launcher da interface gráfica)
│   ├── quick_start.py           (Guia de início rápido)
│   └── exemplos_avancados.py    (Exemplos de uso avançado)
│
├── 📚 Documentação
│   ├── README.md                (Documentação principal)
│   ├── INSTALACAO.md            (Guia de instalação passo a passo)
│   └── PROJECT_STRUCTURE.md     (Este arquivo)
│
├── ⚙️ Configuração
│   ├── requirements.txt          (Dependências Python)
│   └── .env.example             (Template de variáveis de ambiente)
│
└── 💾 Runtime
    └── conversas_salvas/        (Conversas salvas automaticamente)
```

---

## 📄 Descrição dos Arquivos

### 🤖 Núcleo do Agente

#### `gemini_agent.py` ⭐
**Arquivo principal** contém a classe `GeminiAgent` que implementa:

- **Métodos principais:**
  - `__init()` - Inicializa com chave API
  - `chat()` - Conversa com histórico
  - `process_task()` - Processa tarefas
  - `analyze_text()` - Analisa textos
  - `generate_ideas()` - Gera ideias criativas
  - `solve_problem()` - Resolve problemas
  - `get_conversation_history()` - Retorna histórico
  - `clear_history()` - Limpa histórico
  - `set_system_prompt()` - Customiza comportamento

- **Tamanho:** ~300 linhas
- **Dependências:** google-generativeai
- **Uso:** Base para todas as aplicações

#### `gui.py`
**Interface gráfica completa** com Tkinter:

- **3 Abas:**
  1. 💬 **Chat** - Conversa com histórico colorido
  2. 📋 **Tarefas** - Processamento de tarefas específicas
  3. 📚 **Histórico** - Gerenciamento de conversas salvas

- **Funcionalidades:**
  - Chat interativo com timestamps
  - Processamento assíncrono (não congela UI)
  - Salvamento de conversas em JSON
  - Tema escuro profissional
  - Múltiplas tarefas disponíveis

- **Tamanho:** ~500 linhas
- **Dependências:** tkinter (built-in)
- **Uso:** Interface visual principal

#### `hello.py`
**Exemplo de uso básico** do agente:

- 4 exemplos práticos:
  1. Conversa simples
  2. Processamento de tarefa
  3. Geração de ideias
  4. Resolução de problema

- **Tamanho:** ~50 linhas
- **Uso:** Teste inicial e aprendizado

---

### 🚀 Inicializadores

#### `run_gui.py`
**Launcher da interface gráfica:**

- Verifica ambiente
- Valida chave API
- Carrega interface com validações
- Mensagens de erro úteis

- **Uso:** `python run_gui.py`

#### `quick_start.py`
**Guia interativo de início:**

- Verifica ambiente completo
- Mostra funcionalidades
- Fornece exemplos em Python
- Solução de problemas
- Dicas úteis

- **Uso:** `python quick_start.py`

#### `exemplos_avancados.py`
**8 exemplos de uso avançado:**

1. Conversa com contexto progressivo
2. Processamento em lote (batch)
3. Análise de múltiplos textos
4. Resolver com contexto e restrições
5. Gerador de ideias temático
6. Sistema prompt customizado
7. Salvar/carregar histórico
8. Análise avançada de texto

- **Tamanho:** ~400 linhas
- **Uso:** `python exemplos_avancados.py`

---

### 📚 Documentação

#### `README.md`
**Documentação principal completa:**

- Visão geral do projeto
- Funcionalidades
- Pré-requisitos e instalação
- Exemplos de uso
- Métodos disponíveis
- Troubleshooting
- Tips avançadas

#### `INSTALACAO.md`
**Guia passo a passo de instalação:**

- Pré-requisitos
- Obter chave API
- Instalar dependências
- Configurar chave (3 métodos)
- Verificar instalação
- Segurança
- Problemas comuns

#### `PROJECT_STRUCTURE.md`
**Este arquivo** - estrutura e descrição do projeto

---

### ⚙️ Configuração

#### `requirements.txt`
**Dependências do projeto:**

```
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

- `google-generativeai` - API do Gemini
- `python-dotenv` - Carrega variáveis de .env

#### `.env.example`
**Template de variáveis de ambiente:**

```
GEMINI_API_KEY=sua-chave-aqui
```

- Copie para `.env` local
- Adicione sua chave real
- Não commite `.env` no Git

---

### 💾 Runtime

#### `conversas_salvas/`
**Diretório criado automaticamente:**

- Armazena conversas em JSON
- Nomes: `conversa_YYYYMMDD_HHMMSS.json`
- Gerenciado pela interface GUI
- Fácil backup e análise

---

## 🔄 Fluxo de Execução

### Fluxo 1: Interface Gráfica (Recomendado)
```
run_gui.py
    ↓
Verifica ambiente
    ↓
Carrega gui.py
    ↓
Inicializa GeminiAgent
    ↓
Abre interface Tkinter
    ↓
Usuário interage
    ↓
Salva conversas em conversas_salvas/
```

### Fluxo 2: Exemplos Simples
```
hello.py
    ↓
Inicializa GeminiAgent
    ↓
Executa 4 exemplos
    ↓
Exibe resultados
```

### Fluxo 3: Exemplos Avançados
```
exemplos_avancados.py
    ↓
Menu interativo
    ↓
Seleciona exemplo
    ↓
Executa exemplo selecionado
    ↓
Salva resultados em arquivo JSON
```

### Fluxo 4: Uso em Python
```
import GeminiAgent
    ↓
Cria instância
    ↓
Chama métodos específicos
    ↓
Processa respostas
```

---

## 🛠️ Casos de Uso

| Caso | Arquivo | Descrição |
|------|---------|-----------|
| Uso geral | `run_gui.py` | Interface visual completa |
| Aprendizado | `hello.py` | Exemplos básicos |
| Avançado | `exemplos_avancados.py` | Uso profissional |
| Integração | `gemini_agent.py` | Biblioteca Python |
| Diagnóstico | `quick_start.py` | Verificar setup |

---

## 📊 Estatísticas do Projeto

| Métrica | Valor |
|---------|-------|
| Arquivos Python | 7 |
| Linhas de código | ~1500+ |
| Documentação | 3 arquivos |
| Funcionalidades | 8+ |
| Abas GUI | 3 |
| Exemplos | 12+ |
| Modelos suportados | 3+ |

---

## 🔐 Segurança

### Boas Práticas Implementadas:

✅ Chave API em variável de ambiente
✅ Suporte a arquivo .env separado
✅ Validações de entrada
✅ Tratamento de erros
✅ Histórico seguro em JSON local
✅ Sem logging de credenciais

### O que evitar:

❌ Não hardcode a chave no código
❌ Não commite .env no Git
❌ Não compartilhe sua chave API
❌ Não exponha a chave em logs

---

## 🚀 Performance

### Otimizações:

- ⚡ Processamento assíncrono na GUI
- 📦 Lazy loading de dependências
- 💾 Cache de histórico
- 🔄 Reconexão automática
- 📊 Compressão de JSON

### Limitações Conhecidas:

- Rate limit: 15 req/min (plano gratuito)
- Tamanho histórico: Limitar a ~100 mensagens
- Timeout: 30 segundos por padrão

---

## 🔄 Integração com Outros Projetos

### Como Usar em Outro Projeto:

1. Copie `gemini_agent.py` para seu projeto
2. Instale dependência: `pip install google-generativeai`
3. Configure variável de ambiente
4. Importe e use:

```python
from gemini_agent import GeminiAgent

agent = GeminiAgent()
response = agent.chat("Sua pergunta aqui")
```

---

## 📈 Roadmap Futuro

- [ ] Suporte a múltiplos modelos
- [ ] Integração com banco de dados
- [ ] API REST
- [ ] Web interface
- [ ] Exportar para PDF
- [ ] Integração com Discord/Slack
- [ ] Análise de sentimentos avançada
- [ ] Tradução multilíngue

---

## 📞 Suporte

Para problemas ou dúvidas:

1. Leia `INSTALACAO.md`
2. Execute `python quick_start.py`
3. Consulte `README.md`
4. Verifique `exemplos_avancados.py`

---

**Desenvolvido com ❤️ usando Gemini AI**
