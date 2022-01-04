

class TD_Generator:

    def __init__(self, query_results):
        self.query_results = query_results # json format
        self.TDs_list = []
        self.rendered_query_results = []
        self.template = "" # path to template
        pass


    def generate_td(self):
        pass


    def load_template(self):
        pass


    def info_to_render(self):
        pass


    def store_TDs(self):
        pass


    def render_query_results(self):
        pass


    def main_generation(self):
        # Call triple store with Triple_Store_Controller using execute_sparql_query(query) function
        # Call render_query_results to render the list to make it more accesible
        # Call load_template function to load the template
        # Make for loop (result in self.query_results)
            # Call info_to_render function to append result info to a dictionary that is going to be used to render the template loaded
            # Call generate_td to generate all TDs, all of these TDs have to be stored in a list
        # Call store_TDs to store inside wot-hive or Thing Directory (TDD) one by one the TDs stored in the TDs_list
        pass