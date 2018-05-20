# visualize-geo-data
位置情報データを可視化するプログラム

## Requirements
- Python3.6
- pipenv

## Setup

```
$ pipenv install
```

## Help

oオプションで出力するファイル名を変更できます。(default: map.html)  
tオプションでマップを変更できます。

```
$ ./visualize-geo.py --help
Usage: visualize-geo.py [OPTIONS]

Options:
  -o, --output TEXT  Output HTML
  -t, --tile TEXT    choose map design:
                     mapboxbright
                     cartodbdark_matter
                     cartodbpositron
                     cloudmade
                     mapbox
                     mapboxcontrolroom
                     openstreetmap
                     stamenterrain
                     stamentoner
                     stamenwatercolor
  --help             Show this message and exit.
```

# Input
CSV形式。  
1列目は緯度, 2列目は経度, 3列目はコメント(3列目は必ずしも必要としない)

## Usage

```
cat sample.csv | ./visualize-geo.py
```
