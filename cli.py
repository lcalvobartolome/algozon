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
import argparse
import datetime

from cart import Cart
from rich.console import Console  # type: ignore
from rich.table import Table  # type: ignore

from core import Batch, Catalog, Product, Stock
from customers import (BusinessCustomer, EmployeeCustomer, GuestCustomer,
                       IndividualCustomer, TaxExemptBusinessCustomer)
from pricing import PricingPolicy
from reports import SalesLedger

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

# ---------------------------------------------------------------------------
# Estado compartido del sistema (instancias de prueba)
# ---------------------------------------------------------------------------

# Catálogo
catalog = Catalog()
catalog.add_product(Product("A-001", "YOGUR", "alimentación"))
catalog.add_product(Product("A-020", "LECHE", "alimentación"))
catalog.add_product(Product("A-046", "PAN",   "alimentación"))

# Stock
stock = Stock()
stock.add_shipment(Batch("B1", "A-001", 10, 1.0, datetime.date(2026, 12, 31)))
stock.add_shipment(Batch("B2", "A-001",  5, 1.2, datetime.date(2026, 11, 30)))
stock.add_shipment(Batch("B3", "A-020", 10, 0.8, datetime.date(2026, 10, 15)))
stock.add_shipment(Batch("B4", "A-046",  8, 0.5, datetime.date(2026,  9, 20)))

# Ledger y política de precios
ledger = SalesLedger()
pricing_policy = PricingPolicy(logistics_rate=0.60, profit_rate=0.05)
date = datetime.date(2026, 3, 11)


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


def run_demo() -> int:
    """Ejecuta un escenario completo sin interacción del usuario.

    Cubre los cinco tipos de cliente con una compra simulada cada uno:
      1. GuestCustomer        — compra 2 YOGUR, elegible, gana (simulado).
      2. IndividualCustomer   — compra 3 LECHE, elegible, pierde (simulado).
      3. BusinessCustomer     — compra 2 PAN,   no elegible.
      4. TaxExemptBusiness    — compra 2 YOGUR, no elegible.
      5. EmployeeCustomer     — compra 2 LECHE, no elegible.

    Muestra por cada compra:
      - label() del cliente y elegibilidad para minijuego.
      - Líneas registradas (lote, uds, gross_price_unit) y precio neto total.
      - Precio final pagado según fiscalidad del cliente.

    Al finalizar imprime el beneficio por producto y el beneficio total.

    Ejecuta en base al estado compartido definido en este módulo (catalog, stock, ledger, pricing_policy) al principio del archivo.

    Returns
    -------
    int
        0 si el escenario completa sin errores.
    """
    console.print(
        "\n[bold cyan]══════════════════════════════════════[/bold cyan]")
    console.print(
        "[bold cyan]   ALGOZON — DEMO PARA INVERSORES      [/bold cyan]")
    console.print(
        "[bold cyan]══════════════════════════════════════[/bold cyan]\n")

    #########################
    # Catálogo de productos #
    #########################
    console.print("[bold]Catálogo de productos:[/bold]")
    filas_catalogo = []
    # catalog.get_products() devuelve una lista de Product, y stock.available_stock(product_id) devuelve el stock disponible para ese producto_id. Se itera sobre los productos del catálogo para mostrar su información junto con el stock disponible.
    for p in catalog.get_products():
        fila = [p.product_id, p.name, p.category,
                str(stock.available_stock(p.product_id))]
        filas_catalogo.append(fila)
    # display_table() es una función helper definida en este módulo que utiliza Rich para mostrar una tabla formateada. Se le pasan dos argumentos: una lista de encabezados para las columnas y una lista de filas, donde cada fila es una lista de valores correspondientes a cada columna
    display_table(["ID", "Producto", "Categoría",
                  "Stock disponible"], filas_catalogo)

    #########################
    # Política de precios   #
    #########################
    console.print(
        f"\n[bold]Política de precios:[/bold]  "
        f"logistics_rate={pricing_policy.get_logistics_rate():.0%}  |  "
        f"profit_rate={pricing_policy.get_profit_rate():.0%}  |  IVA=21%\n"
    )

    # Escenario simulado: 5 clientes, cada uno con una compra diferente
    c1 = GuestCustomer("C1", "John Doe", "john.doe@mail.com")
    c2 = IndividualCustomer("C2", "Carlos Ruiz", "carlos@mail.com")
    c3 = BusinessCustomer("C3", "TechCorp S.L.", "tech@corp.com")
    c4 = TaxExemptBusinessCustomer("C4", "Univ. Pública", "univ@edu.es")
    c5 = EmployeeCustomer("C5", "María López", "maria@algozon.com")

    # Cada entrada es: (cliente, producto_id, cantidad, ganó_minijuego)
    scenario = [
        (c1, "A-001", 2, True),
        (c2, "A-020", 3, True),
        (c3, "A-046", 2, False),
        (c4, "A-001", 2, False),
        (c5, "A-020", 2, False),
    ]

    for customer, product_id, qty, simulated_won in scenario:

        # Nombre del producto para mostrarlo
        product_name = product_id
        for p in catalog.get_products():
            if p.product_id == product_id:
                product_name = p.name

        console.rule(
            f"[bold magenta]{customer.label()}[/bold magenta]"
            f"  ·  {customer.name}  ·  {qty}x {product_name}"
        )

        # Elegibilidad
        eligible = customer.is_eligible_for_minigame()
        eligible_str = "[green]Sí[/green]" if eligible else "[red]No[/red]"
        console.print(f"  Elegible para minijuego : {eligible_str}")

        if eligible:
            won = simulated_won
            res = "[green]VICTORIA[/green]" if won else "[red]DERROTA[/red]"
            console.print(f"  Resultado simulado      : {res}")
        else:
            won = False

        # Carrito -> reserva -> checkout
        cart = Cart(customer.customer_id)
        try:
            cart.add(stock, product_id, qty)
            receipt = cart.checkout(
                stock, ledger, pricing_policy, date, customer, won
            )
        except Exception as e:
            print_error(f"Error en la compra: {e}")
            continue

        # Líneas del recibo
        console.print("\n  [bold]Líneas registradas:[/bold]")
        table_rows = []
        for lines in receipt.values():
            for line in lines:
                fila = [
                    product_name,
                    line["batch_id"],
                    str(line["quantity"]),
                    f"{line['unit_cost']:.4f} €",
                    f"{line['gross_price_unit']:.4f} €",
                ]
                table_rows.append(fila)
        display_table(["Producto", "Lote", "Uds", "Coste unit.",
                      "Gross price unit."], table_rows)

        # Totales de esta compra
        final_paid = sum(
            line["gross_price_unit"] * line["quantity"]
            for lines in receipt.values()
            for line in lines
        )

        console.print(f"  Precio bruto total      : {final_paid:.4f} €")
        console.print(
            f"  [bold green]Precio final pagado     : {final_paid:.2f} €[/bold green]"
        )

        if isinstance(customer, GuestCustomer) and won:
            print_warning(
                "  ¡Crea una cuenta para disfrutar del descuento en futuras compras!"
            )

    # Resumen del ledger
    console.print()
    console.rule("[bold cyan]RESUMEN AlgoZon[/bold cyan]")

    profit_pp = ledger.profit_per_product()
    console.print("\n  [bold]Beneficio por producto:[/bold]")
    profit_rows = []
    for pid, profit in profit_pp.items():
        product_name = pid
        for p in catalog.get_products():
            if p.product_id == pid:
                product_name = p.name
        profit_rows.append([product_name, f"{profit:.4f} €"])
    display_table(["Producto", "Beneficio bruto"], profit_rows)

    console.print(
        f"\n  Facturación bruta total    : [bold]{ledger.total_gross():.4f} €[/bold]")
    console.print(
        f"  Beneficio total AlgoZon    : [bold green]{ledger.total_profit():.4f} €[/bold green]")

    console.print()
    print_success("Escenario demo completado correctamente.")
    return 0


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
        return run_demo()
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
