def read_wimbledon_data(filename):
    champions = {}  # Dictionary to store champions and their win counts
    countries = set()  # Set to store countries of champions

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # Skip the header line
        next(in_file)

        for line in in_file:
            data = line.strip().split(",")
            champion = data[2]
            country = data[1]

            if champion in champions:
                champions[champion] += 1
            else:
                champions[champion] = 1

            countries.add(country)

    return champions, sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    print("\nThese countries have won Wimbledon:")
    countries_string = ", ".join(countries)
    print(countries_string)


def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)
    display_champions(champions)
    display_countries(countries)


main()
