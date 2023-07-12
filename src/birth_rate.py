import pandas as pd

class US_Births:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        
    def read_csv(self):
        self.data = pd.read_csv(self.file_path)
        print("CSV file successfully loaded.")

    def remove_columns(self, columns):
        self.data.drop(columns=columns, inplace=True)
        print("Columns successfully removed.")
        
    def get_data(self):
        return self.data

    def state_keyword_query(self, keyword):
        matching_states = [state for state in self.data['State'].unique() if keyword in state]
        print(f"Matching State for keyword '{keyword}':")
        for State in matching_states:
            print(State)

    def sort_data(self):
        sorted_data = self.data.sort_values(by=['State', 'Education Level of Mother'])
        combined_data = sorted_data.groupby(['State', 'Year', 'Education Level of Mother']).agg({
            'Number of Births': 'sum',
            'Average Age of Mother (years)': lambda x: round(x.mean(), 1)
        }).reset_index()
        return combined_data

if __name__ == "__main__":
    file_path = '../Data/us_births_2016_2021.csv'       
    data_processor = US_Births(file_path)
    data_processor.read_csv()

    # remove columns
    columns_to_remove = ['State Abbreviation', 'Average Birth Weight (g)', 'Gender']  
    data_processor.remove_columns(columns_to_remove)
    
    #creates clean DF
    cleaned_data = data_processor.get_data()
    cleaned_data.to_csv('../Data/Cleaned_Births.csv', index=False)
    print("Cleaned data saved as 'Cleaned_Births.csv'.")

    keyword = 'keyword'  # Replace 'keyword' with your desired keyword
    data_processor.state_keyword_query(keyword)

    combined_data = data_processor.sort_data()
    combined_data.to_csv('../Data/Avg_Mothers_Birth.csv', index=False)
    print("Cleaned data saved as 'Avg_Mothers_Birth.csv'.")