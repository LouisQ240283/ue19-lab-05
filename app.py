import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("type") == "single":
            print(f"\n{data['joke']}\n")
        elif data.get("type") == "twopart":
            print(f"\n{data['setup']}")
            print(f"{data['delivery']}\n")
        else:
            print("Impossible de récupérer une blague.")
    except requests.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

if __name__ == "__main__":
    print("=== Bienvenue dans JokeAPI CLI ===")
    get_joke()
