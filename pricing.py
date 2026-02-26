class PricingPolicy:

    def __init__(
        self,
        logistics_rate: float,
        profit_rate: float
    ) -> None:
        self._logistics_rate = logistics_rate
        self._profit_rate = profit_rate

    def get_logistics_rate(self) -> float:
        return self._logistics_rate
    
    def get_profit_rate(self) -> float:
        return self._profit_rate
    
    def net_price(self, unit_cost: float) -> float:
        c_log = unit_cost * (1 + self._logistics_rate)
        return c_log * (1 + self._profit_rate)

    def gross_price(self, net_price: float, tax_rate: float) -> float:
        return net_price * (1 + tax_rate)

    def price_breakdown(self, unit_cost: float, tax_rate: float = None) -> dict:
        c_log     = unit_cost * (1 + self._logistics_rate)
        net       = self.net_price(unit_cost)
        gross     = self.gross_price(net, tax_rate) if tax_rate is not None else None

        return {
            "unit_cost":      unit_cost,
            "logistics_cost": unit_cost * self._logistics_rate,
            "profit_margin":  c_log * self._profit_rate,
            "net_price":      net,
            "gross_price":    gross
        }