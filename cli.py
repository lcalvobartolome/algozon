import argparse
from rich.console import Console  # type: ignore
from rich.table import Table  # type: ignore

console = Console()


BANNER = r"""
 █████╗ ██╗      ██████╗  ██████╗ ███████╗ ██████╗ ███╗   ██╗    ██████╗ ██████╗ ███╗   ███╗
██╔══██╗██║     ██╔════╝ ██╔═══██╗╚══███╔╝██╔═══██╗████╗  ██║   ██╔════╝██╔═══██╗████╗ ████║
███████║██║     ██║  ███╗██║   ██║  ███╔╝ ██║   ██║██╔██╗ ██║   ██║     ██║   ██║██╔████╔██║
██╔══██║██║     ██║   ██║██║   ██║ ███╔╝  ██║   ██║██║╚██╗██║   ██║     ██║   ██║██║╚██╔╝██║
██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║ ╚████║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝

                              ⇢  Welcome to AlgoZon CLI  ⇠
"""


# =========================
# Utils
# =========================
def print_banner(force_plain: bool = False) -> None:
    """
    Prints AlgoZon banner to the console.

    Parameters:
    -----------
    force_plain: bool
        If True, prints the banner without colors.
    """
    if force_plain:
        console.print(BANNER)
    else:
        console.print(BANNER, style="bold green")


# =========================
# CLI Helpers
# =========================
# Importante: Estas funciones son de ayuda. Se deberán adaptar o ampliar
# según las necesidades de los ejercicios.
# =========================
def display_menu(title: str, options: list[str]) -> int:
    """
    Displays a numbered menu and prompts user to select an option.

    Parameters:
    -----------
    title: str
        Title of the menu to display.
    options: list[str]
        List of option names to display.

    Returns:
    --------
    int
        Index (0-based) of the selected option.
    """
    console.print(f"\n[bold cyan]{title}[/bold cyan]")
    console.print("─" * 50)

    for idx, option in enumerate(options, start=1):
        console.print(f"  [bold]{idx}.[/bold] {option}")

    console.print("─" * 50)

    while True:
        try:
            choice = console.input(
                "[bold yellow]Selecciona una opción: [/bold yellow]")
            idx = int(choice) - 1

            if 0 <= idx < len(options):
                return idx
            else:
                console.print(
                    f"[red]Error: Selecciona un número entre 1 y {len(options)}[/red]")
        except ValueError:
            console.print("[red]Error: Introduce un número válido[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Operación cancelada[/yellow]")
            raise SystemExit(0)


def display_table(headers: list[str], rows: list[list[str]]) -> None:
    """
    Displays data in a formatted table using Rich.

    Parameters:
    -----------
    headers: list[str]
        Column headers for the table.
    rows: list[list[str]]
        List of rows, where each row is a list of values.
    """
    table = Table(show_header=True, header_style="bold magenta")

    for header in headers:
        table.add_column(header)

    for row in rows:
        table.add_row(*row)

    console.print(table)


def prompt_input(prompt_text: str, input_type: type = str) -> any:
    """
    Prompts user for input with validation.

    Parameters:
    -----------
    prompt_text: str
        Text to display when prompting.
    input_type: type
        Expected type of input (str, int, float).

    Returns:
    --------
    any
        User input converted to the specified type.
    """
    while True:
        try:
            value = console.input(f"[bold yellow]{prompt_text}[/bold yellow] ")

            if input_type == str:
                return value
            elif input_type == int:
                return int(value)
            elif input_type == float:
                return float(value)
            else:
                return input_type(value)
        except ValueError:
            console.print(
                f"[red]Error: Introduce un valor válido de tipo {input_type.__name__}[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Operación cancelada[/yellow]")
            raise SystemExit(0)


def confirm_action(message: str) -> bool:
    """
    Asks user for yes/no confirmation.

    Parameters:
    -----------
    message: str
        Confirmation message to display.

    Returns:
    --------
    bool
        True if user confirms (y/yes), False otherwise.
    """
    while True:
        try:
            response = console.input(
                f"[bold yellow]{message} (s/n): [/bold yellow]").lower().strip()

            if response in ['s', 'si', 'sí', 'y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                console.print(
                    "[red]Error: Responde con 's' (sí) o 'n' (no)[/red]")
        except KeyboardInterrupt:
            console.print("\n[yellow]Operación cancelada[/yellow]")
            raise SystemExit(0)


def print_success(message: str) -> None:
    """Prints a success message in green."""
    console.print(f"[bold green]✓ {message}[/bold green]")


def print_error(message: str) -> None:
    """Prints an error message in red."""
    console.print(f"[bold red]✗ {message}[/bold red]")


def print_info(message: str) -> None:
    """Prints an informational message in cyan."""
    console.print(f"[cyan]ℹ {message}[/cyan]")


def print_warning(message: str) -> None:
    """Prints a warning message in yellow."""
    console.print(f"[yellow]⚠ {message}[/yellow]")


# =========================
# Demo Functions
# =========================
def test_helpers_demo() -> None:
    """
    Demonstrates all CLI helper functions.
    """
    print_info("Iniciando demostración de funciones helper...")

    # Demo: display_menu
    console.print(
        "\n[bold magenta]1. Demostración de display_menu()[/bold magenta]")
    customer_types = ["Cliente Invitado", "Cliente de Empresa Registrado"]
    selected_idx = display_menu(
        "Selecciona un tipo de cliente", customer_types)
    print_success(f"Has seleccionado: {customer_types[selected_idx]}")

    # Demo: display_table
    console.print(
        "\n[bold magenta]2. Demostración de display_table()[/bold magenta]")
    print_info("Mostrando catálogo de productos...")
    display_table(
        ["ID", "Producto", "Precio", "Stock"],
        [
            ["A-001", "Laptop Dell XPS", "1299.99€", "5"],
            ["A-002", "Mouse Logitech", "29.99€", "15"],
            ["A-003", "Teclado Mecánico", "89.99€", "0"],
            ["B-001", "Monitor 4K", "449.99€", "8"],
        ]
    )

    # Demo: prompt_input
    console.print(
        "\n[bold magenta]3. Demostración de prompt_input()[/bold magenta]")
    product_id = prompt_input("Introduce un ID de producto (ej. A-001):", str)
    print_success(f"ID introducido: {product_id}")

    quantity = prompt_input("Introduce cantidad:", int)
    print_success(f"Cantidad introducida: {quantity}")

    # Demo: confirm_action
    console.print(
        "\n[bold magenta]4. Demostración de confirm_action()[/bold magenta]")
    confirmed = confirm_action("¿Deseas añadir este producto al carrito?")

    if confirmed:
        print_success("Producto añadido al carrito")
    else:
        print_warning("Operación cancelada por el usuario")

    # Demo: mensajes de estado
    console.print(
        "\n[bold magenta]5. Demostración de mensajes de estado[/bold magenta]")
    print_success("Esta es una operación exitosa")
    print_error("Este es un mensaje de error (OutOfStockError)")
    print_info("Este es un mensaje informativo")
    print_warning("Esta es una advertencia")

    console.print("\n[bold green]✓ Demostración completada[/bold green]")


# =========================
# CLI
# =========================
def build_parser() -> argparse.ArgumentParser:
    """
    Builds the argument parser for the CLI.

    Returns:
    --------
    argparse.ArgumentParser
        Configured argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="python3 cli.py",
        description="AlgoZon.com — Core System CLI",
    )

    parser.add_argument(
        "--option",
        dest="cmd",
        required=True,
        choices=["demo", "checkout", "test-helpers"],
        help="Selecciona qué ejecutar: demo, checkout o test-helpers"
    )

    parser.add_argument(
        "--force-plain",
        action="store_true",
        help="Muestra el banner sin códigos de color ANSI"
    )

    return parser


def main() -> int:
    """Main function for the CLI.

    Returns:
    --------
    int
        Exit code of the program:
        - 0: Success
        - 1: Failure
    """
    parser = build_parser()
    args = parser.parse_args()

    print_banner(force_plain=args.force_plain)

    if args.cmd == "demo":
        ################################################################
        # TODO: Sustituir este bloque por el escenario demo real       #
        console.print("[bold cyan]Ejecutando el escenario demo...[/bold cyan]")
        return 0
        ################################################################

    elif args.cmd == "checkout":
        ################################################################
        # TODO: Sustituir este bloque por el checkout interactivo real #
        console.print(
            "[bold cyan]Ejecutando el escenario checkout...[/bold cyan]")
        return 0
        ################################################################

    elif args.cmd == "test-helpers":
        test_helpers_demo()
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
