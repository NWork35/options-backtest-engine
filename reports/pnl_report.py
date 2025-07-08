class PnLReport:
    def __init__(self, trades, config):
        self.trades = trades
        self.config = config

    def generate_summary(self):
        total_pnl = sum(t["pnl"] for t in self.trades)
        win_trades = [t for t in self.trades if t["pnl"] > 0]
        loss_trades = [t for t in self.trades if t["pnl"] <= 0]

        print("📈 Backtest Summary")
        print("====================")
        print(f"Total Trades: {len(self.trades)}")
        print(f"Winning Trades: {len(win_trades)}")
        print(f"Losing Trades: {len(loss_trades)}")
        print(f"Net PnL: ₹{total_pnl:,.2f}")
        print("====================")

