import pandas as pd

df = pd.read_csv("Elevation NYC.csv")
east_harlem = df[
    (df['Latitude'] >= 40.7915) & (df['Latitude'] <= 40.8080) &
    (df['Longitude'] >= -73.9520) & (df['Longitude'] <= -73.9280)
]
east_harlem.to_csv("East_Harlem_Elevation.csv", index=False)