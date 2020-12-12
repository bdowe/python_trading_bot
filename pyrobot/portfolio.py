from typing import List, Dict, Union, Optional, Tuple

class Portfolio():
    def __init__(self, account_number: Optional[str]):
        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0
        self.account_number = account_number
    
    def add_position(self, symbol: str, asset_type: str, purchase_date: Optional[str], quantity: int = 0, purchase_price: float = 0.0) -> dict:
        self.positions[symbol] = {
            'symbol': symbol,
            'quantity': 0,
            'purchase_price': purchase_price,
            'purchase_date': purchase_date,
            'asset_type': asset_type,
        }

        return self.positions
    
    def add_positions(self, positions: List[dict]) -> dict:
        assert isinstance(positions, list)

        for _, position in enumerate(positions):
            self.add_position(
                symbol = position.symbol,
                asset_type = position.asset_type,
                purchase_date = position.get('purchase_date', None),
                purchase_price = position.get('purchase_price', 0.0),
                quantity = position.get('quantity', 0.0),
            )
        
        return self.positions

    def remove_position(self, symbol: str) -> Tuple[bool, str]:
        if symbol in self.positions:
            del self.positions[symbol]
            return (True, "{symbol} was successfully removed".format(symbol=symbol))
        else:
            return (False, "{symbol} did not exist in the portfolio".format(symbol=symbol))

    def is_profitable(self, symbol: str, current_price: float) -> bool:
        purchase_price = self.positions[symbol]['purchase_price']

        return purchase_price <= current_price

    def total_allocation(self):
        pass

    def risk_exposure(self):
        pass

    def in_portfolio(self, symbol: str) -> bool:
        pass

    def total_market_value(self):
        pass
            
