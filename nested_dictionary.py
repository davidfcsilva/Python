{
  key: [List],
  key2: {Dict},
}

visited_cities = {
  "France": "Paris",
  "Germany": "Berlin",
} 

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}

cities_visited = {
  "France": {
    "Paris": "Visited 2 times",
    "Lille": "Visited 1 time",
    "Dijon": "Visited 4 times",},
  "Germany": {
    "Berlin": "Visited 1 time",
    "Hamburg": "Visited 3 times",
    "Stuttgard": "Visited 5 times",},
}

travel_log_v2 = {
  "France": {"cities_visited_v2": ["Paris", "Lille", "Dijon"], "total_visits": 5},
  "Germany": {"cities_visited_v2": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 5},
}

travel_log_list = [
  {
    "country": "France",
    "cities_visited_v2": ["Paris", "Lille", "Dijon"], 
    "total_visits": 5,
  },
  {
    "country": "Germany",
    "cities_visited_v2": ["Berlin", "Hamburg", "Stuttgard"],
    "total_visits": 5,
  },
]

print(visited_cities)
print(travel_log)
print(cities_visited)
