# AlgoZon.com

> **Repositorio template para ejercicios y prácticas en Python**  
> Fundamentos de simulación para telecomunicaciones  
> Grado en Ingeniería de Comunicaciones Móviles y Espaciales  
> Curso 2025/2026

---

<div align="center">
<img src="static/algozon_robot.png" alt="AlgoZon Robot" width="300">
</div>

<div align="center">

**¡FELICIDADES!**

*Acabas de ser contratado como desarrollador freelance por una nueva startup llamada **AlgoZon.com**: un mercado en línea completamente nuevo que quiere redefinir cómo funciona el comercio digital.*

*La plataforma aún no está en línea, pero los inversionistas la están observando de cerca. El objetivo: **máxima automatización, mínima intervención humana y sistemas inteligentes** que se encarguen de todo por sí mismos.*

*Tu misión durante las próximas semanas es construir el núcleo de esta plataforma paso a paso. Los fundadores no quieren una simple tienda en línea; quieren un sistema que se sienta vivo.*

**Tu rol**

*Cada semana ampliarás el sistema, mejorarás su lógica y lo harás más inteligente.*

*Sé creativo, pero preciso.*

*Y recuerda: ¡un mal diseño cuesta dinero!*

**Bienvenido a AlgoZon.**

</div>

## Instrucciones

### 1. Crear repositorio desde la plantilla

Usa este repositorio como plantilla y clónalo localmente:

```bash
git clone https://github.com/tu-usuario/algozon.git
cd algozon
```

### 2. Crear rama propia por integrante

Cada miembro del equipo debe trabajar en su propia rama durante las clases guiadas:

```bash
git checkout -b NIA-integrante
```

### 3. Iteración: Lab II extiende Lab I

Este proyecto es iterativo. Las funcionalidades del Lab II se construyen sobre el Lab I.

### 4. Crear y activar entorno virtual

Crea un entorno virtual para aislar las dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# .venv\Scripts\activate   # En Windows
```

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 5. Ejecutar desde la terminal

Ejecuta el CLI con las siguientes opciones:

```bash
python3 cli.py --option demo            # Ejecutar escenario demo
python3 cli.py --option checkout        # Ejecutar checkout interactivo
python3 cli.py --option test-helpers    # Probar funciones helper del CLI
python3 cli.py --help                   # Ver todas las opciones
```
