class Social ScienceLibrary:
    def __init__(self):
        self.library = {}

    def add_article(self, title, content):
        if title in self.library:
            print("An article with the same title already exists. Use a different title.")
        else:
            self.library[title] = content
            print("Article added successfully.")

    def search_article(self, keyword):
        results = {}
        for title, content in self.library.items():
            if keyword.lower() in content.lower() or keyword.lower() in title.lower():
                results[title] = content
        return results

    def view_article(self, title):
        if title in self.library:
            print(f"Title: {title}\n")
            print(self.library[title])
        else:
            print("Article not found.")

def main():
    library = Social ScienceLibrary()

    while True:
        print("\n==== Social Science Digital Library ====")
        print("1. Add Article")
        print("2. Search Articles")
        print("3. View Article")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            library.add_article(title, content)

        elif choice == "2":
            keyword = input("Enter keyword to search for articles: ")
            results = library.search_article(keyword)
            if results:
                print("\nSearch Results:")
                for title, content in results.items():
                    print(f"\nTitle: {title}\n{content}")
            else:
                print("No matching articles found.")

        elif choice == "3":
            title = input("Enter the title of the article to view: ")
            library.view_article(title)

        elif choice == "4":
            print("Exiting the Social Science Digital Library.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
