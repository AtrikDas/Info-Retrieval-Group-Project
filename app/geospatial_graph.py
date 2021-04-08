import pycountry
import plotly.express as px

class Geospatial_Graph:


    @staticmethod
    def find_iso_aplha(data):
        countries = {}
        for country in pycountry.countries:
            countries[country.name] = country.alpha_3
        codes = [countries.get(country, 'Unknown code') for country in data]
        return codes

    @staticmethod
    def generate_graph():
        df = px.data.gapminder().query("year==2007")
        codes = Geospatial_Graph.find_iso_aplha(df["country"])
        fig = px.choropleth(locations=codes,
                        color=df["lifeExp"],
                        hover_name=df["country"],
                        color_continuous_scale="Bluered_r")
        fig.update_layout(coloraxis_colorbar=dict(
            title="",
            ticks="outside",
            ticktext=["trump", "biden"],
            tickvals= [40, 70]
        ))
        return fig