import pandas as pd
from sqlalchemy import text

from app.database.connection import create_session


def create_dataframe():
    session = create_session()
    query = session.execute(text("SELECT * FROM temperature"))

    df = pd.DataFrame(query.fetchall())

    return df
