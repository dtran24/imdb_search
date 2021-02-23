from utils import json_file_to_dict
from data_prep import DATA_STORE_FP

class IMDBSearchEngine:
    def __init__(self, datastore_fp):
        self.movie2keywords = json_file_to_dict(datastore_fp)

    def search(self, query):
        """ Searches for `query` and returns a list of results
        --- Parameters
        query (str): string used to search data
        """
        movie_keywords_pairs = []
        for i, q in enumerate(query.split()):
            # initializes `movie_keywords_pairs` with first keyword from query
            if i == 0:
                for movie, keywords in self.movie2keywords.items():
                    if q in keywords:
                        movie_keywords_pairs.append((movie, keywords))
            # trims `movie_keywords_pairs` using the remaining keywords from query
            else:
                del_idxs = []
                for j, tple in enumerate(movie_keywords_pairs):
                    movie, keywords = tple
                    if q not in keywords:
                        del_idxs.append(j)

                del_idxs.reverse()
                for j in del_idxs:
                    del movie_keywords_pairs[j]

        return [movie for movie, keywords in movie_keywords_pairs]


if __name__ == '__main__':
    # Example usage
    engine = IMDBSearchEngine(DATA_STORE_FP)
    res = engine.search('spielberg hanks')
    print('Results')
    print(res)
