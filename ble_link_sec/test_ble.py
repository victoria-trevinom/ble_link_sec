import asyncio
import threading
import customtkinter as ctk
from bleak import BleakScanner, BleakClient

# Configuración del tema visual moderno
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class BLEApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("PIA H2 - Enlace Bluetooth Low Energy (BLE)")
        self.geometry("520x560")
        self.resizable(False, False)

        # Título principal
        self.title_label = ctk.CTkLabel(self, text="Scanner & Conector BLE", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=15)

        # Marco de entrada de datos
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(pady=5, padx=20, fill="x")

        self.lbl_name = ctk.CTkLabel(self, text="Nombre Bluetooth del dispositivo móvil:", font=("Arial", 12))
        self.lbl_name.pack(pady=5)

        self.entry_name = ctk.CTkEntry(self, width=320, height=35, placeholder_text="Ej. POCO M5s, Galaxy, etc.")
        self.entry_name.pack(pady=5)
        self.entry_name.insert(0, "POCO M5s") # Valor por defecto editable

        # Botón de acción principal
        self.btn_run = ctk.CTkButton(self, text="📡 Buscar y Conectar al Enlace", command=self.start_connection_thread, fg_color="#1f538d", height=42, font=("Arial", 13, "bold"))
        self.btn_run.pack(pady=15)

        # Caja de registros (Logs) con diseño de consola limpia
        self.log_box = ctk.CTkTextbox(self, width=470, height=180, font=("Consolas", 11))
        self.log_box.pack(pady=5)
        self.log_box.insert("0.0", "[*] Sistema listo. Ingrese el nombre del teléfono y presione conectar.\n")

        # Botón de ayuda / Troubleshooting por si falla
        self.btn_help = ctk.CTkButton(self, text="💡 ¿Qué hacer si no se conecta?", command=self.show_help, fg_color="#4f46e5", height=30)
        self.btn_help.pack(pady=10)

    def log(self, message):
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")

    def show_help(self):
        help_text = (
            "\n--- 🛠️ GUÍA RÁPIDA DE RESOLUCIÓN DE PROBLEMAS ---\n"
            "1. Pantalla abierta: Mantén la pantalla de 'Ajustes > Bluetooth'\n"
            "   abierta en tu celular para obligarlo a anunciarse.\n"
            "2. Distancia: Coloca el teléfono cerca de la laptop (línea de vista).\n"
            "3. Interferencias: Si hay muchos dispositivos, desconecta audífonos\n"
            "   o mouse Bluetooth extras en la laptop.\n"
            "4. Reinicio: Si Android sigue bloqueando la señal, reinicia\n"
            "   el celular e inténtalo de nuevo.\n"
            "--------------------------------------------------\n"
        )
        self.log(help_text)

    def start_connection_thread(self):
        target = self.entry_name.get().strip()
        if not target:
            self.log("[!] Error: El nombre del dispositivo no puede estar vacío.")
            return

        self.btn_run.configure(state="disabled", text="Buscando en el aire...")
        self.entry_name.configure(state="disabled")
        
        # Ejecutar en segundo plano para no congelar la interfaz gráfica
        threading.Thread(target=self.run_async_loop, args=(target,), daemon=True).start()

    def run_async_loop(self, target):
        asyncio.run(self.execute_ble_connection(target))
        # Restaurar botones al terminar
        self.after(0, lambda: self.btn_run.configure(state="normal", text="📡 Buscar y Conectar al Enlace"))
        self.after(0, lambda: self.entry_name.configure(state="normal"))

    async def execute_ble_connection(self, target):
        self.log(f"\n[-] Iniciando escaneo activo para: '{target}'...")
        
        # Animación visual de puntos en consola
        for _ in range(2):
            await asyncio.sleep(0.5)
            
        try:
            device = await BleakScanner.find_device_by_name(target, timeout=12.0)
            
            if not device:
                self.log(f"[!] No se encontró el dispositivo '{target}'.")
                self.log("[!] Sugerencia: Revisa que el Bluetooth de la laptop esté encendido")
                self.log("    y que la pantalla de Bluetooth de tu teléfono esté visible.")
                return

            self.log(f"[+] ¡Dispositivo encontrado exitosamente!")
            self.log(f"    -> Nombre: {device.name}")
            self.log(f"    -> MAC / ID: {device.address}")
            self.log(f"[-] Estableciendo canal de enlace físico BLE...")

            async with BleakClient(device) as client:
                if client.is_connected:
                    self.log(f"[+] ¡ENLACE ESTABLECIDO CON ÉXITO!")
                    self.log(f"[+] Canal de comunicación abierto con {device.address}.")
                    await asyncio.sleep(4.0)
                    self.log(f"[-] Finalizando prueba de enlace de forma segura.")
                    
        except Exception as ex:
            self.log(f"[-] Error crítico en la conexión: {ex}")
            self.log("[-] Tip: Intente reiniciar el Bluetooth de la PC o del teléfono.")

if __name__ == "__main__":
    app = BLEApp()
    app.mainloop()