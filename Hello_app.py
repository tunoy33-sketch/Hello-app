import tkinter as tk
from tkinter import messagebox
import requests

class HelloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello App")
        self.root.geometry("400x300")
        
        # Variables para usuario y contraseña
        self.usuario = tk.StringVar()
        self.contrasena = tk.StringVar()
        self.idioma = tk.StringVar()
        
        # Datos del usuario (simulados para login)
        self.usuario_correcto = "admin"
        self.contrasena_correcta = "1234"
        
        # Crear la interfaz
        self.crear_interfaz()
        
        # Obtener país e idioma
        self.pais, self.idioma_nativo = self.obtener_ubicacion()
    
    def crear_interfaz(self):
        # Frame principal
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)
        
        # Etiqueta de título
        titulo = tk.Label(frame, text="Hello App", font=("Arial", 20, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Campo de usuario
        tk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="e", pady=5)
        entry_usuario = tk.Entry(frame, textvariable=self.usuario, width=25)
        entry_usuario.grid(row=1, column=1, pady=5)
        
        # Campo de contraseña (con asteriscos)
        tk.Label(frame, text="Contraseña:").grid(row=2, column=0, sticky="e", pady=5)
        entry_contrasena = tk.Entry(frame, textvariable=self.contrasena, width=25, show="*")
        entry_contrasena.grid(row=2, column=1, pady=5)
        
        # Botones
        btn_login = tk.Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white")
        btn_login.grid(row=3, column=0, pady=10, padx=5)
        
        btn_logout = tk.Button(frame, text="Logout", command=self.logout, bg="#f44336", fg="white")
        btn_logout.grid(row=3, column=1, pady=10, padx=5)
        
        # Etiqueta para mensajes
        self.etiqueta_mensaje = tk.Label(frame, text="", font=("Arial", 12))
        self.etiqueta_mensaje.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Mostrar ubicación obtenida
        info_ubicacion = f"País detectado: {self.pais} | Idioma: {self.idioma_nativo}"
        tk.Label(frame, text=info_ubicacion, font=("Arial", 10), fg="gray").grid(row=5, column=0, columnspan=2, pady=10)
    
    def obtener_ubicacion(self):
        """Obtiene país e idioma desde la IP del usuario"""
        try:
            # Obtener datos de ubicación desde la IP
            respuesta = requests.get('http://ip-api.com/json/')
            datos = respuesta.json()
            
            pais = datos.get('country', 'Desconocido')
            codigo_pais = datos.get('countryCode', 'US')
            
            # Traducir "Hello" al idioma nativo usando una API
            try:
                respuesta_idioma = requests.get(f'https://api.fourtonfish.com/hellosalut/hello/?cc={codigo_pais}')
                datos_idioma = respuesta_idioma.json()
                saludo = datos_idioma.get('hello', 'Hello')
            except:
                saludo = 'Hello'  # Fallback si la API no responde
            
            return pais, saludo
            
        except:
            return "Desconocido", "Hello"  # Fallback si hay error
    
    def login(self):
        """Simula el inicio de sesión"""
        usuario = self.usuario.get().strip()
        contrasena = self.contrasena.get().strip()
        
        # Validar campos vacíos
        if not usuario or not contrasena:
            messagebox.showerror("Error", "Usuario y contraseña son obligatorios")
            return
        
        # Validar credenciales (simuladas)
        if usuario == self.usuario_correcto and contrasena == self.contrasena_correcta:
            mensaje = f"{self.idioma_nativo} {usuario}! Has iniciado sesión correctamente!"
            self.etiqueta_mensaje.config(text=mensaje, fg="green")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def logout(self):
        """Simula el cierre de sesión"""
        usuario = self.usuario.get().strip()
        
        if usuario:
            mensaje = f"¡Que tengas un gran día, {usuario}!"
        else:
            mensaje = "¡Que tengas un gran día!"
        
        self.etiqueta_mensaje.config(text=mensaje, fg="blue")
        self.usuario.set("")
        self.contrasena.set("")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()
