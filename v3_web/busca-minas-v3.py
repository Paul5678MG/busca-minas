#Importando modulos para clases abstractas y biblioteca random
from abc import ABC, abstractmethod
import random
import flet as ft

#Interfaz para las casillas
class CasillaMolde(ABC):
    @abstractmethod
    def revelar(self):
        pass
    
    @abstractmethod
    def es_bomba(self):
        pass
    
    @abstractmethod
    def probabilidad(self):
        pass

#Casilla con gema
class CasillaDiamante(CasillaMolde):
    def revelar(self):
        return "💎"
    
    def es_bomba(self):
        return False
    
    def probabilidad(self):
        return 0.65

#Casilla con dinero
class CasillaDinero(CasillaMolde):
    def revelar(self):
        return "💸"
    
    def es_bomba(self):
        return False
    
    def probabilidad(self):
        return 0.1

#Casilla con bomba
class CasillaBomba(CasillaMolde):
    def revelar(self):
        return "💥"
    
    def es_bomba(self):
        return True
    
    def probabilidad(self):
        return 0.25

class GeneradorTablero:
    def __init__(self, multiplicador, lista_recompensas):
        self.multiplicador = multiplicador
        self.cantidad = multiplicador * multiplicador
        self.lista_recompensas = list(lista_recompensas)

    def generar_casilla(self):
        lista_resultado = list()
        probabilidades = [r.probabilidad() for r in self.lista_recompensas]
        
        for _ in range(1, self.cantidad+1):
            resultado = random.choices(
                population = self.lista_recompensas,
                weights= probabilidades,
                k=1
            )[0]
            lista_resultado.append(type(resultado)())
        return lista_resultado

#Función principal, page lienzo en blanco
def main(page: ft.Page):
    page.title = "Buscaminas - Paul Edition"
    #Agregando icono para la web
    page.window_icon = "assets/favicon.png"
    #Evita que el usuario tenga que hacer scroll si el tablero es grande
    page.scroll = ft.ScrollMode.AUTO 
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    estado = {
        "casillas_tipos": [CasillaDiamante(), CasillaDinero(), CasillaBomba()],
        "multiplicador": None,
        "ultimo_btn_tamaño": None,
        "casillas": [],
        "recompensas_obtenidas": dict()
    }
    
    #Funcion para seleccionar el tamaño de las cuadriculas
    def seleccionar_tamaño(e):
        if estado["ultimo_btn_tamaño"] == e.control:
            e.control.bgcolor = "#1E1C4D"
            e.control.update()
            estado["multiplicador"] = None
            estado["ultimo_btn_tamaño"] = None
            mensaje_error.visible = False
            return
        
        if estado["ultimo_btn_tamaño"]:
            estado["ultimo_btn_tamaño"].bgcolor = "#1E1C4D"  
            estado["ultimo_btn_tamaño"].update()
            
        estado["multiplicador"] = e.control.data
        e.control.bgcolor = "#00DDFF"
        e.control.update()
        
        estado["ultimo_btn_tamaño"] = e.control
        mensaje_error.visible = False
        mensaje_error.update()
    
    def revelar_casilla_click(e):
        casilla_click = e.control.data
        
        e.control.content = ft.Text(casilla_click.revelar(), size=20)
        
        if casilla_click.es_bomba():
            btn_retirar.disabled = True
            btn_retirar.visible = False
            mensaje_error.visible = True
            e.control.bgcolor = "#FF2E63"
            mensaje_error.value = "¡BOOM! GAME OVER 💀"
            mensaje_error.color = "#FF2E63"
            casillas_grid = contenedor_tablero.controls[0]
            for c in casillas_grid.controls:
                if c == e.control:
                    c.disabled = True
                    continue
                
                if c.bgcolor == "#08D9D6":
                    c.disabled = True
                    continue
                
                casilla_grid = c.data
                c.content = ft.Text(casilla_grid.revelar(), size=20)
                
                if casilla_grid.es_bomba():
                    c.bgcolor = "#853749"
                else:
                    c.bgcolor = "#4A8A89"
                c.opacity = 0.2
                c.disabled = True     
            page.update()
        else:
            estado["recompensas_obtenidas"][casilla_click.revelar()] = estado["recompensas_obtenidas"].get(casilla_click.revelar(),0) + 1
            btn_retirar.visible = True
            e.control.bgcolor = "#08D9D6"
            e.control.disabled = True
            e.control.update() 
            btn_retirar.update()
    
    #Mensaje para visualizar ganancia
    mensaje_ganancia = ft.Text("", weight="bold", color="#00FF08",visible=False)
    #Mensaje para capturar errores
    mensaje_error = ft.Text("", weight="bold", color="#FF2E63",visible=False)
    #Mensaje para capturar avisos
    mensaje_aviso = ft.Text("", weight="bold", color="#FF9100",visible=False)
    
    #Contenedor para cuadriculas
    contenedor_tablero = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    #Función para mostrar mensaje de ganancia conseguida
    def retirar_ganancias(e):
        casillas_grid = contenedor_tablero.controls[0]
        for c in casillas_grid.controls:
            if c == e.control:
                c.disabled = True
                continue
            
            if c.bgcolor == "#08D9D6":
                c.disabled = True
                continue
            
            casilla_grid = c.data
            c.content = ft.Text(casilla_grid.revelar(), size=20)
            
            if casilla_grid.es_bomba():
                c.bgcolor = "#853749"
            else:
                c.bgcolor = "#4A8A89"
            c.opacity = 0.2
            c.disabled = True                
        btn_retirar.disabled = True
        mensaje_ganancia.visible = True
        mensaje = "GANASTE:"
        for c in estado["casillas_tipos"]:
            if c.revelar() in estado["recompensas_obtenidas"]:
                mensaje += f" {estado['recompensas_obtenidas'].get(c.revelar(),0)} {c.revelar()}"
        mensaje_ganancia.value = mensaje
    
    #Funcion para crear las cuadriculas
    def jugar():
        estado["recompensas_obtenidas"] = dict()
        btn_retirar.disabled = False
        btn_retirar.visible = False
        mensaje_ganancia.visible = False
        estado["gemas_obtenidas"] = 0
        multiplicador = estado["multiplicador"]
        if not multiplicador:
            mensaje_error.visible = True
            mensaje_error.value = "⚠️ Selecciona un tamaño antes de empezar"
            mensaje_error.update()
            return
        mensaje_error.visible = False
        
        recompensas = [CasillaDiamante(), CasillaDinero(), CasillaBomba()]
        generador_tablero = GeneradorTablero(estado["multiplicador"], recompensas)
        estado["casillas"] = generador_tablero.generar_casilla()
        
        grid = ft.GridView(runs_count=multiplicador, spacing=5, run_spacing=5, width=300)
        
        for casilla in estado["casillas"]:
            grid.controls.append(
                ft.Container(
                    content=ft.Text(""), 
                    bgcolor="#1E1C4D",
                    width=40, height=40,
                    border_radius=5,
                    alignment=ft.Alignment(0, 0),
                    data = casilla, 
                    on_click=revelar_casilla_click
                )
            )
        
        titulo.size = 45
        mensaje_aviso.visible = True
        mensaje_aviso.value = "⚠️¡CUIDADO! 1 de cada 4 casillas es una GRANADA 💥"
        contenedor_tablero.controls = [grid] # Metemos el grid al contenedor
        page.update(titulo)
    
    titulo = ft.Text("Busca Minas", size=180, weight = "bold", color= "dark-blue")
    
    #Botones para elegir tamaño de cuadriculas
    btn_3x3 = ft.Button("3x3", data=3, color="white", bgcolor = "#1E1C4D", on_click=seleccionar_tamaño)
    btn_5x5 = ft.Button("5x5", data = 5, color="white", bgcolor = "#1E1C4D", on_click=seleccionar_tamaño)
    btn_7x7 = ft.Button("7x7", data = 7, color="white",bgcolor = "#1E1C4D", on_click=seleccionar_tamaño)
    btn_9x9 = ft.Button("9x9", data = 9,color="white", bgcolor = "#1E1C4D", on_click=seleccionar_tamaño)
    fila_tamaños = ft.Row(
        controls=[btn_3x3, btn_5x5, btn_7x7, btn_9x9],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    #Boton para retirar ganancias
    btn_retirar = ft.ElevatedButton(
        content=ft.Text("RETIRARSE", color="white", size=14, weight="bold"),
        bgcolor="#00FF08",  
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20), 
            overlay_color="#FFCC00",  
            padding=ft.padding.symmetric(horizontal=60, vertical=14),  
        ),
        on_click=retirar_ganancias,
        visible=False
    )
    
    #Boton para empezar
    btn_empezar = ft.ElevatedButton(
        content=ft.Text("JUGAR", color="white", size=14, weight="bold"),
        bgcolor="#1E1C4D",  
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20), 
            overlay_color="#00FF08",  
            padding=ft.padding.symmetric(horizontal=135, vertical=14),  
        ),
        on_click=jugar
    )
    
    #Agregando objetos al lienzo
    page.add(titulo, mensaje_aviso, ft.Divider(height=20, color="dark-blue"),contenedor_tablero, ft.Divider(height=20, color="dark-blue"), fila_tamaños, mensaje_ganancia, mensaje_error, btn_retirar, btn_empezar)

#Ejecutar la aplicación
ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=8080)

