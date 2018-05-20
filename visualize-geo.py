#!/usr/bin/env python
import folium
import sys
import pandas as pd
import click


@click.command()
@click.option("-o", "--output", default="map.html", help="Output HTML file name")
def main(output):
    japan_map = folium.Map(location=[35, 135], zoom_start=5, tiles='Stamen Terrain')
    df = pd.read_csv(sys.stdin, header=None)
    geos = df.values.tolist()
    if len(geos[0]) < 3:
        return 0
    for g in geos:
        folium.Marker(location=[g[0], g[1]], popup=g[2]).add_to(japan_map)
    japan_map.save(output)
    return None


if __name__ == "__main__":
    main()
