import plotly.plotly as py
from plotly.graph_objs import *

fig = {
    'data': [
        {
            'labels': ['1st', '2nd', '3rd', '4th', '5th'],
            'values': [38, 27, 18, 10, 7],
            'type': 'pie',
            'name': 'Starry Night',
            'marker': {'colors': ['rgb(56, 75, 126)',
                                  'rgb(18, 36, 37)',
                                  'rgb(34, 53, 101)',
                                  'rgb(36, 55, 57)',
                                  'rgb(6, 4, 4)']},
            'domain': {'x': [0, .48],
                       'y': [0, .49]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        },
        {
            'labels': ['1st', '2nd', '3rd', '4th', '5th'],
            'values': [28, 26, 21, 15, 10],
            'marker': {'colors': ['rgb(177, 127, 38)',
                                  'rgb(205, 152, 36)',
                                  'rgb(99, 79, 37)',
                                  'rgb(129, 180, 179)',
                                  'rgb(124, 103, 37)']},
            'type': 'pie',
            'name': 'Sunflowers',
            'domain': {'x': [.52, 1],
                       'y': [0, .49]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'

        },
        {
            'labels': ['1st', '2nd', '3rd', '4th', '5th'],
            'values': [38, 19, 16, 14, 13],
            'marker': {'colors': ['rgb(33, 75, 99)',
                                  'rgb(79, 129, 102)',
                                  'rgb(151, 179, 100)',
                                  'rgb(175, 49, 35)',
                                  'rgb(36, 73, 147)']},
            'type': 'pie',
            'name': 'Irises',
            'domain': {'x': [0, .48],
                       'y': [.51, 1]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        },
        {
            'labels': ['1st', '2nd', '3rd', '4th', '5th'],
            'values': [31, 24, 19, 18, 8],
            'marker': {'colors': ['rgb(146, 123, 21)',
                                  'rgb(177, 180, 34)',
                                  'rgb(206, 206, 40)',
                                  'rgb(175, 51, 21)',
                                  'rgb(35, 36, 21)']},
            'type': 'pie',
            'name':'The Night Café',
            'domain': {'x': [.52, 1],
                       'y': [.51, 1]},
            'hoverinfo':'label+percent+name',
            'textinfo':'none'
        }
    ],
    'layout': {'title': 'Van Gogh: 5 Most Prominent Colors Shown Proportionally',
               'showlegend': False}
}

py.iplot(fig, filename='pie_chart_subplots')