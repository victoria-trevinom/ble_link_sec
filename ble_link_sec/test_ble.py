"""Interfaz grÃ¡fica interactiva (GUI) con CustomTkinter y Bleak."""
import threading
import asyncio
import customtkinter as ctk
from ble_link_sec.red import calcular_distancia_rssi
from ble_link_sec.interop import escanear_dispositivos


class AppBLE(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PIA H3 - BLE Link Security Tool")
        self.geometry("600x500")

        self.label = ctk.CTkLabel(
            self, text="Panel de Control BLE",
            font=("Arial", 20, "bold")
        )
        self.label.pack(pady=15)

        self.btn_scan = ctk.CTkButton(
            self, text="Escanear Dispositivos",
            command=self.iniciar_escaneo
        )
        self.btn_scan.pack(pady=10)

        self.textbox = ctk.CTkTextbox(self, width=540, height=300)
        self.textbox.pack(pady=10)

    def iniciar_escaneo(self):
        self.textbox.delete("1.0", "end")
        self.textbox.insert(
            "end", "Escaneando dispositivos...\n"
        )

        def run_async():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            coro = escanear_dispositivos(4)
            dispositivos = loop.run_until_complete(coro)

            msg = f"Se encontraron {len(dispositivos)} dispositivos.\n"
            self.textbox.insert("end", msg)
            for d in dispositivos:
                dist = calcular_distancia_rssi(d["rssi"])
                linea = (
                    f"Nombre: {d['nombre']}\n"
                    f"  MAC: {d['direccion']} | "
                    f"RSSI: {d['rssi']} dBm | "
                    f"Dist: {dist:.2f}m\n"
                    "----------------------------------------\n"
                )
                self.textbox.insert("end", linea)

        threading.Thread(target=run_async, daemon=True).start()


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = AppBLE()
    app.mainloop()
