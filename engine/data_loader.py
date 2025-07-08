import requests
import pandas as pd

class DataLoader:
    def __init__(self, config):
        self.config = config
        self.token = config.get("dhan_token")
        self.headers = {
            "accept": "application/json",
            "access-token": self.token,
        }

    def load(self):
        if self.config.get("data_source") == "csv":
            return self._load_from_csv()
        else:
            return self._load_from_dhan()

    def _load_from_csv(self):
        spot = pd.read_csv(self.config["spot_csv"], parse_dates=["timestamp"])
        options = pd.read_csv(self.config["option_csv"], parse_dates=["timestamp"])
        return {"spot": spot, "options": options}

    def _load_from_dhan(self):
        print("🔄 Fetching data from Dhan API (limited sample logic)...")

        # Example: You should build a looped fetch per symbol & date
        # Here’s one dummy call
        url = "https://api.dhan.co/historical/instruments/intraday"
        params = {
            "securityId": "1333",  # example ID, replace as needed
            "exchangeSegment": "NSE_INDEX",
            "instrument": "Nifty Bank",
            "interval": "ONE_MINUTE",
            "from": self.config["start_date"],
            "to": self.config["end_date"],
        }

        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            print("❌ Failed to fetch data:", response.text)
            return {"spot": None, "options": None}

        data = response.json()
        spot_df = pd.DataFrame(data.get("data", []))

        # Add your CE/PE fetch here similarly
        return {"spot": spot_df, "options": None}

