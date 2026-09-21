# PNG Smart Irrigation Calculator
print("=== PNG IRRIGATION SYSTEM ===")

crop = input("Enter crop (kaukau/taro/corn): ")
area = float(input("Enter garden size in m2: "))
soil = input("Enter soil type (sandy/clay/loam): ")

# Simple calculation
if soil == "sandy":
    water_per_m2 = 6
elif soil == "clay":
    water_per_m2 = 4
else:
    water_per_m2 = 5

total_water = area * water_per_m2

print(f"\nFor {area}m2 of {crop} on {soil} soil:")
print(f"You need {total_water} liters per day")
print(f"Water in morning: {total_water/2}L")
print(f"Water in evening: {total_water/2}L")
print("\nIrrigation saved to GitHub!")
