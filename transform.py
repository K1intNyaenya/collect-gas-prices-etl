import json
import pandas as pd
from pathlib import Path

def transform():
    file_path = Path(__file__).resolve().parent / "gas_prices.json"

    with open(file_path, "r") as f:
        data = json.load(f)

    state_data = data["result"]["state"]
    city_data = data["result"]["cities"]

    df_state = pd.DataFrame(state_data)
    df_cities = pd.DataFrame(city_data)

    df_state.columns = df_state.columns.str.lower()
    df_cities.columns = df_cities.columns.str.lower()

    num_cols = ["gasoline", "midgrade", "premium", "diesel"]

    for col in num_cols:
        df_cities[col] = pd.to_numeric(df_cities[col], errors="coerce")
        df_state[col] = pd.to_numeric(df_state[col], errors="coerce")

    print("STATE DATA")
    print(df_state.head())

    print("\nCITY DATA")
    print(df_cities.head())

    return df_state, df_cities

if __name__ == "__main__":
    transform()