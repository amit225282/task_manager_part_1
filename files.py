import pickle

def load_tasks(file="tasks.pickle"):
    """ 
    This function loads the data (default="tasks.pickle"). If there is no data, it creates a new file with empty list.
    """
    try:
        with open (file, 'rb') as f:
            tasks=pickle.load(f)
            return tasks
    except:
         with open (file, 'wb') as f:
            pickle.dump([], f)
            return []
         


def save_tasks(file="tasks.pickle", tasks=[]):
    """
    This function saves the data (default="tasks.pickle").
    """
    with open(file, "wb") as f:
        pickle.dump(tasks, f)



def setup_categories(categories_file="categories.pickle"):
    '''This function creates a file with categories list.'''
    with open (categories_file, 'wb') as f:
        categories=["clean", "work", "money", "family"]
        pickle.dump(categories, f)
        return categories


def load_categories(categories_file="categories.pickle"):
    """ 
    This function loads the data (default="categories.pickle"). If there is no data, it creates a new file with empty list.
    """
    try:
        with open (categories_file, 'rb') as f:
            categories=pickle.load(f)
            return categories
    except:
         with open (categories_file, 'wb') as f:
            pickle.dump([], f)
            return []
         


def save_categories(categories_file="categories.pickle", categories=[]):
    """
    This function saves the data (default="categories.pickle").
    """
    with open (categories_file, "wb") as f:
        pickle.dump(categories, f)




