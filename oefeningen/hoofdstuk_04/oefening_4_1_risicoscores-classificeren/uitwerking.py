scores = [25, 60, 85, 40, 90]
aantal_hoog = 0

for score in scores:
    if score >= 70:
        print(score, "Hoog")
        aantal_hoog += 1
    else:
        print(score, "Laag of middel")

print("Aantal hoge scores:", aantal_hoog)
