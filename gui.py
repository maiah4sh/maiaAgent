"""
Interface Gráfica para o Agente IA Gemini
Aplicação visual com Tkinter para interagir com o agente de forma intuitiva.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, ttk
import threading
from datetime import datetime
import json
from pathlib import Path
from gemini_agent import GeminiAgent


class GeminiAgentGUI:
    """Interface gráfica para o Agente Gemini."""
    
    def __init__(self, root):
        """Inicializa a interface gráfica."""
        self.root = root
        self.root.title("🤖 Agente IA com Gemini")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Variáveis
        self.agent = None
        self.is_loading = False
        self.conversations_dir = Path("conversas_salvas")
        self.conversations_dir.mkdir(exist_ok=True)
        
        # Cores tema
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.accent_color = "#3498db"
        self.user_color = "#2ecc71"
        self.agent_color = "#e74c3c"
        
        self.setup_ui()
        self.show_welcome_dialog()
        self.initialize_agent()
    
    def setup_ui(self):
        """Configura a interface do usuário."""
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color, height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🤖 Agente IA Gemini",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Assistente inteligente alimentado por IA",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#95a5a6"
        )
        subtitle_label.pack()
        
        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Aba 1: Chat
        self.create_chat_tab()
        
        # Aba 2: Tarefas
        self.create_tasks_tab()
        
        # Aba 3: Histórico
        self.create_history_tab()
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#34495e", height=50)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        status_label = tk.Label(
            footer_frame,
            text="Status: Pronto | Desenvolvido com Gemini AI",
            font=("Arial", 9),
            bg="#34495e",
            fg="#95a5a6"
        )
        status_label.pack(pady=12)
        self.status_label = status_label
    
    def create_chat_tab(self):
        """Cria a aba de chat."""
        chat_frame = ttk.Frame(self.notebook)
        self.notebook.add(chat_frame, text="💬 Chat", padding=10)
        
        # Área de conversa
        conversation_label = tk.Label(
            chat_frame,
            text="Histórico da Conversa",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        conversation_label.pack(anchor="w", pady=(0, 5))
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            height=20,
            width=100,
            wrap=tk.WORD,
            bg="#2c3e50",
            fg=self.fg_color,
            font=("Courier", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.chat_display.config(state=tk.DISABLED)
        
        # Tags para colorir texto
        self.chat_display.tag_config("user", foreground=self.user_color, font=("Arial", 10, "bold"))
        self.chat_display.tag_config("agent", foreground=self.agent_color, font=("Arial", 10, "bold"))
        self.chat_display.tag_config("timestamp", foreground="#95a5a6", font=("Arial", 8))
        self.chat_display.tag_config("separator", foreground="#7f8c8d")
        
        # Frame para entrada
        input_frame = tk.Frame(chat_frame, bg="#f0f0f0")
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        input_label = tk.Label(
            input_frame,
            text="Digite sua mensagem:",
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        input_label.pack(anchor="w", pady=(0, 5))
        
        self.chat_input = tk.Text(
            input_frame,
            height=4,
            width=100,
            wrap=tk.WORD,
            font=("Arial", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            bg="#ecf0f1"
        )
        self.chat_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Botões
        button_frame = tk.Frame(input_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X)
        
        send_btn = tk.Button(
            button_frame,
            text="📤 Enviar",
            command=self.send_message,
            bg=self.accent_color,
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        send_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Limpar",
            command=self.clear_chat,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT)
        
        save_btn = tk.Button(
            button_frame,
            text="💾 Salvar",
            command=self.save_conversation,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        save_btn.pack(side=tk.RIGHT)
    
    def create_tasks_tab(self):
        """Cria a aba de tarefas."""
        tasks_frame = ttk.Frame(self.notebook)
        self.notebook.add(tasks_frame, text="📋 Tarefas", padding=10)
        
        # Tipo de tarefa
        type_frame = tk.Frame(tasks_frame, bg="#f0f0f0")
        type_frame.pack(fill=tk.X, pady=(0, 10))
        
        type_label = tk.Label(
            type_frame,
            text="Tipo de Tarefa:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        type_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.task_type = ttk.Combobox(
            type_frame,
            values=[
                "Processar Tarefa",
                "Analisar Texto",
                "Gerar Ideias",
                "Resolver Problema"
            ],
            state="readonly",
            font=("Arial", 10),
            width=25
        )
        self.task_type.set("Processar Tarefa")
        self.task_type.pack(side=tk.LEFT)
        
        # Entrada de tarefa
        task_label = tk.Label(
            tasks_frame,
            text="Descreva sua tarefa:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        task_label.pack(anchor="w", pady=(10, 5))
        
        self.task_input = scrolledtext.ScrolledText(
            tasks_frame,
            height=8,
            width=100,
            wrap=tk.WORD,
            font=("Arial", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            bg="#ecf0f1"
        )
        self.task_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Resultado
        result_label = tk.Label(
            tasks_frame,
            text="Resultado:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        result_label.pack(anchor="w", pady=(10, 5))
        
        self.task_result = scrolledtext.ScrolledText(
            tasks_frame,
            height=10,
            width=100,
            wrap=tk.WORD,
            bg="#2c3e50",
            fg=self.fg_color,
            font=("Courier", 10),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.task_result.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Botões
        button_frame = tk.Frame(tasks_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X)
        
        execute_btn = tk.Button(
            button_frame,
            text="⚡ Executar",
            command=self.execute_task,
            bg=self.accent_color,
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        execute_btn.pack(side=tk.LEFT)
        
        copy_btn = tk.Button(
            button_frame,
            text="📋 Copiar",
            command=self.copy_result,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        copy_btn.pack(side=tk.LEFT, padx=(5, 0))
    
    def create_history_tab(self):
        """Cria a aba de histórico."""
        history_frame = ttk.Frame(self.notebook)
        self.notebook.add(history_frame, text="📚 Histórico", padding=10)
        
        # Lista de conversas salvas
        list_label = tk.Label(
            history_frame,
            text="Conversas Salvas:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        list_label.pack(anchor="w", pady=(0, 5))
        
        # Listbox
        self.history_listbox = tk.Listbox(
            history_frame,
            font=("Arial", 10),
            bg="#ecf0f1",
            height=10,
            relief=tk.FLAT
        )
        self.history_listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.history_listbox.bind('<<ListboxSelect>>', self.load_conversation)
        
        # Conteúdo da conversa
        content_label = tk.Label(
            history_frame,
            text="Conteúdo da Conversa:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        )
        content_label.pack(anchor="w", pady=(10, 5))
        
        self.history_content = scrolledtext.ScrolledText(
            history_frame,
            height=10,
            width=100,
            wrap=tk.WORD,
            bg="#2c3e50",
            fg=self.fg_color,
            font=("Courier", 9),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.history_content.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Botões
        button_frame = tk.Frame(history_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X)
        
        refresh_btn = tk.Button(
            button_frame,
            text="🔄 Atualizar",
            command=self.refresh_history,
            bg=self.accent_color,
            fg="white",
            font=("Arial", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        refresh_btn.pack(side=tk.LEFT)
        
        delete_btn = tk.Button(
            button_frame,
            text="🗑️ Deletar",
            command=self.delete_conversation,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        delete_btn.pack(side=tk.LEFT, padx=(5, 0))
    
    def show_welcome_dialog(self):
        """Mostra instruções ao abrir a interface."""
        message = (
            "Bem-vindo ao Agente IA Gemini!\n\n"
            "1. Configure sua chave GEMINI_API_KEY no sistema.\n"
            "2. Use a aba 'Chat' para conversar com o assistente.\n"
            "3. Use a aba 'Tarefas' para processar prompts e gerar resultados.\n"
            "4. Use a aba 'Histórico' para visualizar e carregar conversas salvas.\n\n"
            "Como conversar com o agente:\n"
            "- Pergunte diretamente: \"Qual é a diferença entre Python e Java?\"\n"
            "- Peça uma lista: \"Liste 5 dicas para estudar programação.\"\n"
            "- Peça um resumo: \"Resuma este texto em 3 frases.\"\n"
            "- Peça um plano: \"Monte um plano de estudos para IA em 4 semanas.\"\n"
            "- Peça uma solução: \"Como otimizar um código Python lento?\"\n\n"
            "Dica: seja claro e específico para obter respostas mais úteis.\n"
            "Você pode salvar conversas no formato JSON a qualquer momento."
        )
        messagebox.showinfo("Como usar", message)
    
    def initialize_agent(self):
        """Inicializa o agente em thread."""
        def load_agent():
            try:
                self.agent = GeminiAgent()
                self.update_status("✓ Agente inicializado com sucesso!")
                self.add_to_chat("Sistema", "Agente pronto para usar!", "timestamp")
            except ValueError as e:
                messagebox.showerror(
                    "Erro",
                    f"Erro ao inicializar: {e}\n\n"
                    "Configure GEMINI_API_KEY na variável de ambiente."
                )
                self.update_status("✗ Erro ao inicializar agente")
        
        thread = threading.Thread(target=load_agent, daemon=True)
        thread.start()
    
    def send_message(self):
        """Envia mensagem ao agente."""
        if not self.agent:
            messagebox.showwarning("Aviso", "Agente ainda não está inicializado")
            return
        
        message = self.chat_input.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Aviso", "Digite uma mensagem")
            return
        
        self.add_to_chat("Você", message, "user")
        self.chat_input.delete("1.0", tk.END)
        
        # Processa em thread
        def process():
            self.is_loading = True
            self.update_status("⏳ Processando...")
            try:
                response = self.agent.chat(message)
                self.add_to_chat("Agente", response, "agent")
            except Exception as e:
                self.add_to_chat("Erro", str(e), "agent")
            finally:
                self.is_loading = False
                self.update_status("✓ Pronto")
        
        thread = threading.Thread(target=process, daemon=True)
        thread.start()
    
    def execute_task(self):
        """Executa uma tarefa."""
        if not self.agent:
            messagebox.showwarning("Aviso", "Agente não inicializado")
            return
        
        task_text = self.task_input.get("1.0", tk.END).strip()
        if not task_text:
            messagebox.showwarning("Aviso", "Digite uma tarefa")
            return
        
        task_type = self.task_type.get()
        self.update_status("⏳ Executando tarefa...")
        
        def execute():
            try:
                if task_type == "Processar Tarefa":
                    result = self.agent.process_task(task_text)
                elif task_type == "Analisar Texto":
                    result = self.agent.analyze_text(task_text)
                elif task_type == "Gerar Ideias":
                    result = self.agent.generate_ideas(task_text)
                elif task_type == "Resolver Problema":
                    result = self.agent.solve_problem(task_text)
                
                self.task_result.config(state=tk.NORMAL)
                self.task_result.delete("1.0", tk.END)
                self.task_result.insert("1.0", result)
                self.task_result.config(state=tk.DISABLED)
                self.update_status("✓ Tarefa concluída")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao executar: {str(e)}")
                self.update_status("✗ Erro ao executar")
        
        thread = threading.Thread(target=execute, daemon=True)
        thread.start()
    
    def add_to_chat(self, sender, message, tag=""):
        """Adiciona mensagem ao chat."""
        self.chat_display.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.chat_display.insert(tk.END, f"{sender}: ", tag)
        self.chat_display.insert(tk.END, f"{message}\n\n")
        self.chat_display.insert(tk.END, "─" * 80 + "\n", "separator")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def clear_chat(self):
        """Limpa o chat."""
        if messagebox.askyesno("Confirmar", "Deseja limpar o histórico do chat?"):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete("1.0", tk.END)
            self.chat_display.config(state=tk.DISABLED)
            if self.agent:
                self.agent.clear_history()
    
    def save_conversation(self):
        """Salva a conversa em arquivo."""
        if not self.agent:
            messagebox.showwarning("Aviso", "Nenhuma conversa para salvar")
            return
        
        history = self.agent.get_conversation_history()
        if not history:
            messagebox.showwarning("Aviso", "Nenhuma mensagem para salvar")
            return
        
        filename = datetime.now().strftime("conversa_%Y%m%d_%H%M%S.json")
        filepath = self.conversations_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        
        messagebox.showinfo("Sucesso", f"Conversa salva em:\n{filename}")
        self.refresh_history()
    
    def refresh_history(self):
        """Atualiza a lista de conversas."""
        self.history_listbox.delete(0, tk.END)
        
        for file in sorted(self.conversations_dir.glob("*.json"), reverse=True):
            self.history_listbox.insert(tk.END, file.name)
    
    def load_conversation(self, event):
        """Carrega uma conversa salva."""
        selection = self.history_listbox.curselection()
        if not selection:
            return
        
        filename = self.history_listbox.get(selection[0])
        filepath = self.conversations_dir / filename
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                history = json.load(f)
            
            self.history_content.config(state=tk.NORMAL)
            self.history_content.delete("1.0", tk.END)
            
            for msg in history:
                timestamp = msg.get("timestamp", "")
                role = msg.get("role", "").upper()
                content = msg.get("content", "")
                
                self.history_content.insert(tk.END, f"[{timestamp}] {role}:\n{content}\n\n")
            
            self.history_content.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar: {str(e)}")
    
    def delete_conversation(self):
        """Deleta uma conversa salva."""
        selection = self.history_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma conversa")
            return
        
        filename = self.history_listbox.get(selection[0])
        if messagebox.askyesno("Confirmar", f"Deletar {filename}?"):
            filepath = self.conversations_dir / filename
            filepath.unlink()
            self.refresh_history()
    
    def copy_result(self):
        """Copia o resultado para clipboard."""
        content = self.task_result.get("1.0", tk.END)
        if content.strip():
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            messagebox.showinfo("Sucesso", "Resultado copiado!")
    
    def update_status(self, message):
        """Atualiza a barra de status."""
        self.status_label.config(text=f"Status: {message}")
        self.root.update()


def main():
    """Função principal."""
    root = tk.Tk()
    app = GeminiAgentGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
