# 💣 Buscaminas - Paul Edition

¡Bienvenido al Buscaminas definitivo! Este proyecto muestra la evolución de un sistema lógico desde una interfaz de consola simple hasta una aplicación gráfica moderna utilizando **Python** y **Flet**.

## 🚀 Evolución del Proyecto

### 🔹 Versión 1: Lógica de Consola (`v1_console`)
La primera etapa se centró en la arquitectura lógica utilizando **Programación Orientada a Objetos (POO)** y principios **SOLID**.
* **Interfaz Basada en Texto:** Selección de casillas mediante números en la terminal.
* **POO Pura y SOLID:** Implementación de `CasillaMolde` (Clase Abstracta) para definir el comportamiento de bombas y casillas normales.
* **Gestión de Tablero:** Creación dinámica de minas basada en un multiplicador (de 2x2 hasta 9x9).

### 🔹 Versión 2: Interfaz Gráfica con Flet (`v2_flet`)
En la segunda versión, el juego dio el salto a una interfaz visual oscura y moderna ("Neon Dark Mode").
* **UI Interactiva:** Tablero visual con botones que cambian de color al ser seleccionados.
* **Sistema de Riesgo/Recompensa:** Nueva mecánica de "Retirarse" para asegurar las gemas obtenidas antes de explotar.
* **Dificultad Dinámica:** Selección de tamaño de tablero (3x3, 5x5, 7x7, 9x9) con generación aleatoria de granadas (aprox. 1/3 del tablero).
* **Feedback Visual:** Animaciones de opacidad y cambios de estado al ganar o perder.

### 🔹 Versión 3: Despliegue Web (Actual)
El estado actual del proyecto, adaptando la potencia de Python al navegador.
* **Web-Ready:** Optimización de assets y rutas para funcionamiento en entornos web.
* **Despliegue Continuo:** Alojado en **Render** mediante contenedores/estáticos.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Lógica:** Clases abstractas (`abc`), manejo de excepciones y biblioteca `random`.
* **Framework UI:** [Flet](https://flet.dev/) (Basado en Flutter).
* **Distribución:** Empaquetado nativo para Windows (.exe) con icono personalizado.
* **Deployment & Hosting:** Render (PaaS).

## 🎮 Cómo Jugar
1.  **Selecciona el tamaño** del tablero en la parte inferior.
2.  Presiona el botón **"JUGAR"**.
3.  Haz clic en las casillas para revelar **Gemas 💎**.
4.  ¡Cuidado! Si tocas una **Granada 💥**, pierdes todo.
5.  Puedes presionar **"RETIRARSE"** en cualquier momento para asegurar tu botín.

## 📦 Instalación y Ejecución
Versión Web (Recomendado)
No necesitas instalar nada. Juega directamente en tu navegador:
🚀 **[Jugar Buscaminas Web](https://busca-minas.onrender.com/)**

Si tienes Python instalado:
```bash
pip install flet
python v2_flet/busca-minas-v2.py

---
Nota: Se contemplan futuras actualizaciones orientadas a la optimización del rendimiento, el refinamiento de las mecánicas de juego y más.

Desarrollado con ❤️ por Paul | 2026