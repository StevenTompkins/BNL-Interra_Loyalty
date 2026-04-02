# Shapefile Centroid Calculator

This program calculates the centroids (latitude and longitude) of zones in a shapefile.

## Requirements

- Python 3.x
- geopandas

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python centroid_calculator.py path/to/your/shapefile.shp
```

The centroids will be saved to `centroids.csv` in the current directory.

## Notes

- The shapefile should include the `.shp` file and associated files (`.dbf`, `.shx`, etc.).
- If the shapefile uses a projected coordinate system, it will be converted to WGS84 (EPSG:4326) for latitude/longitude output.
- Each row in the output CSV corresponds to a zone, with columns: Index, Longitude, Latitude.