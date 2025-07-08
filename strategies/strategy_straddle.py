from .strategy_base import StrategyBase

class StrategyStraddle(StrategyBase):
    def run(self):
        spot_data = self.data["spot"]
        options_data = self.data["options"]

        capital = self.config["capital"]
        sl_pct = self.config["sl_pct"]
        qty = self.config["qty"]

        for index, row in spot_data.iterrows():
            time = row["timestamp"]
            spot = row["close"]

            atm = round(spot / 100) * 100
            ce_symbol = f"BANKNIFTY{atm}CE"
            pe_symbol = f"BANKNIFTY{atm}PE"

            ce_row = options_data[
                (options_data["symbol"] == ce_symbol) &
                (options_data["timestamp"] == time)
            ]
            pe_row = options_data[
                (options_data["symbol"] == pe_symbol) &
                (options_data["timestamp"] == time)
            ]

            if ce_row.empty or pe_row.empty:
                continue

            ce_price = ce_row["ltp"].values[0]
            pe_price = pe_row["ltp"].values[0]

            entry = ce_price + pe_price
            sl_value = entry * sl_pct / 100

            # Dummy exit at EOD (actual SL logic to be added later)
            trade = {
                "time": time,
                "ce_symbol": ce_symbol,
                "pe_symbol": pe_symbol,
                "entry_price": entry,
                "exit_price": entry - sl_value,  # fake SL hit
                "pnl": -sl_value * qty
            }
            self.trades.append(trade)

        return self.trades

