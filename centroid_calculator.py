import geopandas as gpd
import sys
import csv

def main():
    if len(sys.argv) != 2:
        print("Usage: python centroid_calculator.py <path_to_shapefile>")
        sys.exit(1)

    shp_path = sys.argv[1]
    try:
        gdf = gpd.read_file(shp_path)
    except Exception as e:
        print(f"Error reading shapefile: {e}")
        sys.exit(1)

    if gdf.crs is not None and not gdf.crs.is_geographic:
        gdf = gdf.to_crs('EPSG:4326')

    centroids = gdf.centroid

    with open('centroids.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Index', 'Longitude', 'Latitude'])
        for idx, centroid in centroids.items():
            writer.writerow([idx, centroid.x, centroid.y])

    print("Centroids saved to centroids.csv")

if __name__ == "__main__":
    main()