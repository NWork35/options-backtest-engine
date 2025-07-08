class StrategyBase:
    def __init__(self, config, data, risk_engine):
        self.config = config
        self.data = data
        self.risk_engine = risk_engine
        self.trades = []

    def run(self):
        raise NotImplementedError("Each strategy must implement its own run() method.")

