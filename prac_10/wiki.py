import wikipedia


def get_page_summary(title):
    """
    Get and print the title, summary, and URL of a Wikipedia page.

    Parameters:
    - title: The title or search phrase for the Wikipedia page.
    """
    try:
        page = wikipedia.page(title)  # Autosuggest=False was removed due to pycharm's suggestion
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        print("Disambiguation Error: ", e.options)
    except wikipedia.PageError as e:
        print("Page Error: Page not found.")


if __name__ == "__main__":
    search_input = input("Enter a page title or search phrase (blank to exit): ")

    while search_input:
        get_page_summary(search_input)
        print("\n")
        search_input = input("Enter a page title or search phrase (blank to exit): ")