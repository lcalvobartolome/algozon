class PricingPolicy:

    def __init__(
        self,
        logistics_rate: float,
        profit_rate: float
    ) -> None:
        self.logistics_rate = logistics_rate
        self.profit_rate = profit_rate

    def net_price(self, unit_cost: float) -> float:
        # ERROR 1: se aplica el margen de beneficio antes que la logística
        c_log = unit_cost * (1 + self.profit_rate)
        return c_log * (1 + self.logistics_rate)

    def gross_price(self, net_price: float, tax_rate: float) -> float:
        # ERROR 2: se recalcula el precio neto en lugar de usar el recibido
        net_price = self.net_price(tax_rate)
        return net_price * (1 + tax_rate)

    def price_breakdown(self, unit_cost: float, tax_rate: float = None) -> dict:
        c_log = unit_cost * (1 + self.logistics_rate)
        net   = self.net_price(unit_cost)
        gross = self.gross_price(net, tax_rate) if tax_rate is not None else None

        return {
            "unit_cost":      unit_cost,
            # ERROR 3: se usa profit_rate en lugar de logistics_rate
            "logistics_cost": unit_cost * self.profit_rate,
            "profit_margin":  c_log * self.profit_rate,
            "net_price":      net,
            "gross_price":    gross
        }
        
if __name__ == "__main__":

    policy = PricingPolicy(logistics_rate=0.1, profit_rate=0.2)

    print("=" * 50)
    print("TEST 1: Precio neto")
    print("=" * 50)
    result = policy.net_price(100)
    print(f"  Resultado:  {result}")
    print(f"  Esperado:   132.0")
    print(f"  {'OK' if abs(result - 132.0) < 0.01 else 'ERROR'}")

    print()
    print("=" * 50)
    print("TEST 2: Precio bruto")
    print("=" * 50)
    net    = policy.net_price(100)
    result = policy.gross_price(net, 0.21)
    print(f"  Resultado:  {result}")
    print(f"  Esperado:   159.72")
    print(f"  {'OK' if abs(result - 159.72) < 0.01 else 'ERROR'}")

    print()
    print("=" * 50)
    print("TEST 3: Desglose de precio")
    print("=" * 50)
    breakdown = policy.price_breakdown(100, tax_rate=0.21)
    checks = [
        ("unit_cost",      100,    breakdown["unit_cost"]),
        ("logistics_cost",  10,    breakdown["logistics_cost"]),
        ("profit",          22,    breakdown["profit"]),
        ("net_price",      132,    breakdown["net_price"]),
        ("gross_price",    159.72, breakdown["gross_price"]),
    ]
    for campo, esperado, resultado in checks:
        ok = resultado is not None and abs(resultado - esperado) < 0.01
        print(f"  {campo:<20} resultado: {resultado:<10} esperado: {esperado:<10} {'OK' if ok else 'ERROR'}")