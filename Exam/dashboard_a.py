import plotly.express as px
import pandas as pd
from dash import html, dcc
import pycountry

sales = pd.read_csv("Sales.csv")

total_sales_by_year = sales.groupby('Year')['Revenue'].sum().reset_index()
total_sales_by_country = sales.groupby('Country')['Revenue'].sum().reset_index()
sales_by_category = sales.groupby('Product_Category')['Revenue'].sum().reset_index()
monthly_sales = sales.groupby('Month')['Revenue'].sum().reset_index()
average_price_by_year = sales.groupby('Year')['Unit_Price'].mean().reset_index()


def get_country_iso_code(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except:
        return None


total_sales_by_country['ISO_Code'] = total_sales_by_country['Country'].apply(get_country_iso_code)

fig1 = px.bar(total_sales_by_year, x='Year', y='Revenue', title='Общие продажи по годам')
fig2 = px.choropleth(total_sales_by_country, locations='ISO_Code', color='Revenue', title='Продажи по странам')
fig3 = px.pie(sales_by_category, names='Product_Category', values='Revenue', title='Продажи по категориям')
fig4 = px.line(monthly_sales, x='Month', y='Revenue', title='Динамика продаж по месяцам')
fig5 = px.histogram(average_price_by_year, x='Year', y='Unit_Price', title='Средняя цена велосипедов по годам')

layout = html.Div([
    html.H1(children='Дашборд продаж велосипедов'),
    html.Span(children='Анализ продаж велосипедов в Европе.', className='subheader'),

    dcc.Graph(id='graph1', figure=fig1),
    dcc.Graph(id='graph2', figure=fig2),
    dcc.Graph(id='graph3', figure=fig3),
    dcc.Graph(id='graph4', figure=fig4),
    dcc.Graph(id='graph5', figure=fig5)
])
