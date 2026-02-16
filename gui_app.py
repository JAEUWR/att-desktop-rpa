import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import threading
import time
from sheets_handler import SheetsHandler
from ocr_engine import OCREngine
from crm_controller import CRMController

class BotApp:
    def __init__(self, root):
        self.root = root
        self.bot_running = False
        self._setup_ui()
        self.ocr = OCREngine()
        self.sheets = None

    def _setup_ui(self):
        self.root.title("Sistema para Base ATT")
        self.root.configure(bg="#1c1b2f")
        self.root.geometry("700x600")

        tk.Label(self.root, text="SISTEMA PARA BASE ATT", bg="#1c1b2f", fg="#bb86fc", 
                 font=("Segoe UI", 14, "bold")).place(x=10, y=10)

        frame = tk.Frame(self.root, bg="#1c1b2f")
        frame.place(x=10, y=50)

        tk.Button(frame, text="Iniciar Bot", bg="#03dac6", command=self.start_bot).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Detener Bot", bg="#cf6679", fg="white", command=self.stop_bot).pack(side=tk.LEFT, padx=5)

        self.log_widget = scrolledtext.ScrolledText(self.root, height=20, width=85, bg="#121212", fg="#e1e1e1")
        self.log_widget.place(x=10, y=100)

    def log(self, msg):
        self.log_widget.insert(tk.END, f"{msg}\n")
        self.log_widget.see(tk.END)

    def start_bot(self):
        if not self.bot_running:
            self.bot_running = True
            threading.Thread(target=self.ejecutar_ciclo, daemon=True).start()

    def stop_bot(self):
        self.bot_running = False
        self.log("🛑 Bot detenido manualmente.")

    def ejecutar_ciclo(self):
        try:
            self.sheets = SheetsHandler()
            self.log("🚀 Iniciando procesamiento...")
            
            while self.bot_running:
                numero = self.sheets.obtener_siguiente_numero()
                if not numero:
                    self.log("✅ No hay más números por revisar.")
                    break
                
                self.log(f"⏳ Procesando número: {numero}")
                
                # Acciones del CRM
                CRMController.buscar_numero(numero)
                
                # Extracción OCR
                datos_extraidos = self.ocr.extraer_datos()
                
                # Sincronización
                self.sheets.enviar_a_global(datos_extraidos, numero)
                self.sheets.marcar_revisado(numero)
                
                # Cleanup del CRM
                CRMController.limpiar_y_resetear()
                
                self.log(f"✅ Procesado: {numero}")
                time.sleep(3)
                
        except Exception as e:
            self.log(f"❌ Error crítico: {e}")
            self.bot_running = False