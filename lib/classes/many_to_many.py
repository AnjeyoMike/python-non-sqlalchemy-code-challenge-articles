# class Article:
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
        
# # class Author:
# #     def __init__(self, name):
# #         self.name = name

# #     def articles(self):
# #         pass

# #     def magazines(self):
# #         pass

# #     def add_article(self, magazine, title):
# #         pass

# #     def topic_areas(self):
# #         pass

# # class Magazine:
# #     def __init__(self, name, category):
# #         self.name = name
# #         self.category = category

# #     def articles(self):
# #         pass

# #     def contributors(self):
# #         pass

# #     def article_titles(self):
# #         pass

# #     def contributing_authors(self):
# #         pass

class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            article = Article(self, magazine, title)
            return article
        else:
            raise ValueError("Magazine must be a Magazine instance and title must be a string")

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        author_counts = {}
        for article in self._articles:
            if article.author not in author_counts:
                author_counts[article.author] = 0
            author_counts[article.author] += 1
        return [author for author, count in author_counts.items() if count > 2]


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author class")

        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class")

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._author._articles.append(self)
        self._magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise ValueError("Author must be an instance of Author class")

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class")

