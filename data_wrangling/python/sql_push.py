from sqlalchemy import create_engine
import pandas as pd

# Establish connection to SQL
engine = create_engine("mysql://root:password@localhost/nba_players")


def main():
    df = pd.read_csv("final_frame.csv")

    df.to_sql(name="player_stats",index=False,con=engine,if_exists='replace')

if __name__=="__main__":
    main()