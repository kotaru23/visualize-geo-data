#!/usr/bin/env python
import folium
import sys
import pandas as pd
import click
from tqdm import tqdm


@click.command()
@click.option("-o", "--output", default="map.html", help="Output HTML file name")
@click.option("-t", "--tile", default="openstreetmap", help="choose map design:\nmapboxbright\ncartodbdark_matter\ncartodbpositron\ncloudmade\nmapbox\nmapboxcontrolroom\n openstreetmap\nstamenterrain\nstamentoner\nstamenwatercolor")
def main(output, tile):
    japan_map = folium.Map(location=[35, 135], zoom_start=5, tiles=tile)
    df = pd.read_csv(sys.stdin, header=None)
    geos = df.values.tolist()
    for g in tqdm(geos):
        if len(geos[0]) == 3:
            # コメントつきの場合
            folium.Marker(location=[g[0], g[1]], popup=g[2]).add_to(japan_map)
        if len(geos[0]) == 2:
            # 緯度・経度のみの場合
            folium.Marker(location=[g[0], g[1]]).add_to(japan_map)
    japan_map.save(output)
    return None


if __name__ == "__main__":
    main()
