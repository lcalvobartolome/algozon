"""
Utilidades de E/S para el minijuego ASCII de AlgoZon.

Este módulo se proporciona ya implementado. No es necesario modificarlo.
Importa las funciones y el diccionario que necesites en game.py:

    from game_helpers import read_key, clear_screen, wait_key, DIRS

Compatibilidad: Linux, macOS y Windows.
"""

import sys

# ---------------------------------------------------------------------------
# Lectura de teclas sin pulsar Enter
# ---------------------------------------------------------------------------
# La implementación concreta depende del sistema operativo:
#   · Linux / macOS  -> módulos tty y termios (POSIX)
#   · Windows        -> módulo msvcrt
# La detección es automática; el código de game.py no necesita saber cuál
# de las dos se está usando.

try:
    import tty
    import termios

    def read_key() -> str:
        """Lee una sola tecla sin necesitar Enter.

        Returns
        -------
        str
            Carácter leído, convertido a mayúsculas.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            # Restaurar siempre el terminal, incluso si se lanza una excepción
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.upper()

except ImportError:
    # Windows no tiene tty ni termios: usamos msvcrt
    import msvcrt  # type: ignore[import]

    def read_key() -> str:  # type: ignore[no-redef]
        """Lee una sola tecla sin necesitar Enter (versión Windows).

        Returns
        -------
        str
            Carácter leído, convertido a mayúsculas.
        """
        ch = msvcrt.getwch()
        return ch.upper()


def clear_screen() -> None:
    """Borra la pantalla sin parpadeo, usando secuencias de escape ANSI."""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()


def wait_key(prompt: str = "  Pulsa cualquier tecla para continuar...") -> None:
    """Imprime un mensaje y espera a que el usuario pulse cualquier tecla.

    Parameters
    ----------
    prompt : str
        Texto que se mostrará antes de esperar.
    """
    print(prompt)
    read_key()


# ---------------------------------------------------------------------------
# Diccionario de movimientos
# ---------------------------------------------------------------------------
# Convención de coordenadas:
#   - row = 0  →  fila superior del tablero
#   - col = 0  →  columna izquierda del tablero
#   - 'W' (arriba)    → row disminuye  (Δrow = -1)
#   - 'S' (abajo)     → row aumenta    (Δrow = +1)
#   - 'A' (izquierda) → col disminuye  (Δcol = -1)
#   - 'D' (derecha)   → col aumenta    (Δcol = +1)

DIRS: dict[str, tuple[int, int]] = {
    "W": (-1,  0),
    "S": (1,  0),
    "A": (0, -1),
    "D": (0,  1),
}
