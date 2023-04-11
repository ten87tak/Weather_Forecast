import requests

api_key = "bf4c469a6d31cbace0cb71c3e6297762"


def fetch_data(city, nr_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * nr_days
    filtered_data = filtered_data[:nr_values]
    print(filtered_data)
    return filtered_data


if __name__ == "__main__":
    print(fetch_data(city="Tokyo", nr_days=3))

