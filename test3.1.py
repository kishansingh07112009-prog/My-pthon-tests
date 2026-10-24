base_yield = float(input())

rainfall_index = float(input())

soil_quality = float(input())

fertilizer_factor = float(input())

pest_loss = float(input())

yield_estimate = base_yield + rainfall_index * (soil_quality ** fertilizer_factor ) - pest_loss

print(f"{yield_estimate:.2f}")