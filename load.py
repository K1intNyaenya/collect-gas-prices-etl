from sqlalchemy import create_engine
from transform import transform

def load():
    df_state, df_cities = transform()

    av_url = "postgresql+psycopg2://dbuser:password@domain:port/database?sslmode=require"

    engine = create_engine(av_url)

    df_state.to_sql(
        "state_gas_prices",
        engine,       
        index=False,
        if_exists="replace"
    )

    df_cities.to_sql(
        "city_gas_prices",
        engine,          
        index=False,
        if_exists="replace"
    )

    print("Data loaded successfully!")

if __name__ == "__main__":
    load()