def is_year_leap(year):
    if (year % 4 == 0): return True 
    else: return False
year_to_check = 2025
result = is_year_leap(year_to_check)
print(f"год {year_to_check}:{result}")


