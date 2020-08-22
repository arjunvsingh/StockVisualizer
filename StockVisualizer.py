

import datetime
import pandas_datareader.data as web
import dash 
import dash_core_components as dcc     
import dash_html_components as html 
from dash.dependencies import Input, Output  


app = dash.Dash()
app.title ="Stock Visualizer"
app.layout = html.Div(children = [html.H1("Stock Visualization Dashboard"),
                                 html.H4("Please enter stock ticker"),
                                 dcc.Input(id = 'input', value = '',type ='text'),
                                 html.Div(id = 'output-graph')])


def update_value(input_data):
    start = datetime.datetime(2015,1,1)
    end = datetime.datetime.now()
    
    df = web.DataReader(input_data, 'yahoo', start, end)
    
    return dcc.Graph(id = 'example',
                    figure = {
                        'data':[{'x':df.index, 'y': df.Close}],
                        'layout':{'title':input_data}
                        }
                    )


if __name__ == 'main':
    print('Yes')
    app.run_server()

main()


# In[ ]:




