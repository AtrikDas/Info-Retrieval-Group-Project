import pycountry
import plotly.express as px
import pandas as pd

class Geospatial_Graph:
    sentiment_data = pd.read_csv("./static/data/data.csv")
    # sentiment_data.loc[sentiment_data['country'] == "Taiwan", "country"] = "Taiwan, Province of China"
    sentiment_data.loc[sentiment_data['country'] == "Iran", "country"] = "Iran, Islamic Republic of"
    sentiment_data.loc[sentiment_data['country'] == "South Korea", "country"] = "Korea, Republic of"


    @staticmethod
    def find_iso_aplha(data):
        countries = {}
        for country in pycountry.countries:
            countries[country.name] = country.alpha_3
        codes = [countries.get(country, 'Unknown code') for country in data]
        return codes


    @staticmethod
    def generate_graph():
        codes = Geospatial_Graph.find_iso_aplha(Geospatial_Graph.sentiment_data['country'])
        color = ["#FF0000","#add8e6", "#0000FF"]
        fig = px.choropleth(Geospatial_Graph.sentiment_data,locations=codes,
                        color=Geospatial_Graph.sentiment_data["score"],
                        hover_name=Geospatial_Graph.sentiment_data["country"],
                        color_continuous_scale=color,
                        range_color =[-0.15,0.85],
                        hover_data=['Percentage']    
                        ) 
        fig.update_layout(coloraxis_colorbar=dict(
            ticks="outside",
            ticktext=["trump", "biden"],
            tickvals= [-0.15, 0.85],
        ))
        fig.show()
        fig.write_html('1.html')
        return fig

if __name__ == "__main__":
    Geospatial_Graph.generate_graph()