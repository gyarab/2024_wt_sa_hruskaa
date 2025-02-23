import httpx

def get_exchange_rate():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/denni_kurz.txt"
    r = httpx.get(url)
    for line in r.text.split("\n"):
        if "|EUR|" in line:
            return float(line.split("|")[-1].replace(",", "."))

def main():
    rate = get_exchange_rate()
    print(f"Aktuální kurz EUR/CZK: {rate}")
    amount = float(input("Zadejte částku: "))
    print(f"To je {amount / rate:.2f} EUR")

if __name__ == "__main__":
    main()
