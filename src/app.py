import csv
import pandas as pd
from dash import Dash, dcc, dash_table # pip install dash


# get a dataframe with data
file = open("../../printplaydb.csv", "r", encoding="utf8")
db_as_listoflists = list(csv.reader(file))
#print(db_as_listoflists[2][:20])
df = pd.DataFrame(db_as_listoflists, columns = ["id","title","authors","language","type","duration","min_players","max_players","entry_threshold","prep_level","link","hashtags"])
#print(df[["id","title"]])

app = Dash(__name__)
server = app.server

# for options see https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/DataTable/datatable_intro_and_sort.py
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{"name": i, "id": i} for i in df.columns],
    editable=False,
    filter_action="native",
    sort_action="native",
    sort_mode="single"
)

if __name__ == '__main__':
    app.run_server(debug=True)