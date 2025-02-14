import httpx

print("online prevodnik men dle kurzu Ceske narodni banky")

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=189EF7A03CFCE3D9CF6F43DC0F7928A0?date=13.02.2025"

r = httpx.get(url)

lines = r.text.split("\n") 

row = ""
for line in lines:
    if "|EUR|" in line:
        row = line

row_arr = row.split("|")

kurz_str = row_arr[-1]

kurz_str = kurz_str.replace("," , ".")

castka = input("Zadej castku v CZK: ")
result = int(castka) * 25
print(f"To je v EUR: {result}")