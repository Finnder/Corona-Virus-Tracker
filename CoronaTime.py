import requests
import json

# Data From Corona Virus API - Tracks Numbers
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "c6dc03e621mshff752781cf714e6p1321bfjsna514f5021bca"
}
response = requests.request("GET", url, headers=headers)
api = response.json()

# Simplify Information JSON --> Python Code
countryStatsUSA = api["countries_stat"][0]
countryStatsUSACases = api["countries_stat"][0]["cases"]
countryStatsUSADeaths = api["countries_stat"][0]["deaths"]
countryStatsUSACritical = api["countries_stat"][0]["serious_critical"]
countryStatsUSARecovered = api["countries_stat"][0]["total_recovered"]

# Print Information for a more readable version
print("USA Info: " + str(countryStatsUSA) + "\n")
print("Total Deaths In USA: " + str(countryStatsUSADeaths))
print("Total Cases In USA: " + str(countryStatsUSACases))
print("Total Critial Health Victims In USA: " + str(countryStatsUSACritical))
print("Total Recovered Victims In The USA: " + str(countryStatsUSARecovered))
