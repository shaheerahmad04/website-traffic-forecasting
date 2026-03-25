import pandas as pd

file_path = "data/kaggle_web_traffic_dataset_without_missing_values.ts"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find where data starts
data_start = None
for i, line in enumerate(lines):
    if line.strip().lower() == "@data":
        data_start = i + 1
        break

# Extract first data row
first_series = lines[data_start].strip()

# Split page id and series
page_id, series_data = first_series.split(":", 1)

# Split values
values = series_data.split(",")

# Remove the timestamp (first element)
values = values[1:]

# Convert to integers
visitors = []
for v in values:
    try:
        visitors.append(int(v))
    except:
        continue

# Create dataframe
df = pd.DataFrame({
    "Day": range(1, len(visitors) + 1),
    "Visitors": visitors
})

# Save CSV
df.to_csv("data/web_traffic_single_page.csv", index=False)

print("Rows extracted:", len(df))
print("CSV created successfully!")