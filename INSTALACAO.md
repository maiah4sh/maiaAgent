# 📦 Guia de Instalação e Configuração

## Pré-requisitos

- ✅ Windows, macOS ou Linux
- ✅ Python 3.8+
- ✅ Acesso à internet
- ✅ Chave API Gemini (gratuita)

## ⚙️ Passo 1: Obter Chave API

1. Acesse: https://aistudio.google.com/app/apikey
2. Clique em **"Create API Key"**
3. Selecione seu projeto (ou crie um novo)
4. Copie a chave gerada
5. **Guarde em local seguro!**

## 🔧 Passo 2: Clonar/Baixar o Projeto

### Opção A: Via Git
```bash
git clone seu-repositorio
cd seu-repositorio
```

### Opção B: Download Manual
1. Baixe os arquivos
2. Extraia em uma pasta
3. Abra a pasta no terminal

## 📥 Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install google-generativeai
```

## 🔑 Passo 4: Configurar Chave API

### Windows (PowerShell):
```powershell
$env:GEMINI_API_KEY = "sua-chave-aqui"
```

### Windows (CMD):
```cmd
set GEMINI_API_KEY=sua-chave-aqui
```

### Linux/macOS:
```bash
export GEMINI_API_KEY="sua-chave-aqui"
```

### Permanente (Criar arquivo .env):
```bash
# Crie arquivo .env na pasta do projeto:
GEMINI_API_KEY=sua-chave-aqui
```

## ✅ Passo 5: Verificar Instalação

```bash
python quick_start.py
```

Você verá um relatório com:
- ✓ Versão do Python
- ✓ Status da Chave API
- ✓ Dependências instaladas

## 🚀 Passo 6: Iniciar Interface

```bash
python run_gui.py
```

Aguarde o agente carregar (primeira vez pode demorar alguns segundos).

## 📖 Usar em Python

```python
from gemini_agent import GeminiAgent

agent = GeminiAgent()
response = agent.chat("Olá!")
print(response)
```

## 🔒 Segurança

- ⚠️ **Nunca** compartilhe sua chave API
- ⚠️ **Não** cometa a chave no Git
- ✅ Use `.env` para guardar a chave
- ✅ Adicione `.env` ao `.gitignore`

## 🐛 Problemas Comuns

### "ModuleNotFoundError: No module named 'google.generativeai'"
```bash
pip install google-generativeai
```

### "Chave da API não encontrada"
```powershell
# Verifique se a chave está configurada:
$env:GEMINI_API_KEY
# Deve retornar sua chave

# Se retornar vazio, configure novamente:
$env:GEMINI_API_KEY = "sua-chave-aqui"

# Feche e reabra o terminal para aplicar
```

### Interface gráfica não abre em Linux
```bash
sudo apt-get install python3-tk
python run_gui.py
```

### "Rate limit exceeded"
- Aguarde 1 minuto
- Ou considere plano pago

## 📚 Próximos Passos

1. Leia o `README.md` para mais detalhes
2. Execute `python quick_start.py` para dicas
3. Teste a interface com `python run_gui.py`
4. Veja exemplos em `hello.py`

## 💬 Suporte

Se tiver problemas:
1. Verifique se Python 3.8+ está instalado
2. Confirme que a chave API é válida
3. Verifique a conexão com internet
4. Tente atualizar: `pip install --upgrade google-generativeai`

---

**Pronto!** 🎉 Sua interface do Agente Gemini está configurada.

Execute: `python run_gui.py` para começar!
