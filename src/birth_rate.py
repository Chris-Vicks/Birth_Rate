import pandas as pd

# List of states for data processing
states = ['California', 'Illinois', 'North Carolina', 'Oklahoma', 'Texas']

class US_Births:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        """Initialize the US_Births class.

        Parameters:
            file_path (str): Path to the CSV file containing birth data.
        """

#Reads the CSV file and loads the data into the object.        
    def read_csv(self):
        self.data = pd.read_csv(self.file_path)
        print("CSV file successfully loaded.")

#Removes the specified columns from the data.

    def remove_columns(self, columns):
        self.data.drop(columns=columns, inplace=True)
        print("Columns successfully removed.")

    def sum_births_by_year(self, state):
        """Summarizes the number of births by year for a specific state.

        Returns:
            pandas.DataFrame: DataFrame containing the summed data.
        """
        state_data = self.data[self.data['State'] == state]
        summed_data = state_data.groupby(['State', 'Year'])['Number of Births'].sum().reset_index()
        return summed_data
    
    def sum_education_level(self, state):
        education_data = self.data[self.data['State'] == state]
        summed_education_data = education_data.groupby(['State', 'Year', 'Education Level of Mother'])['Number of Births'].sum().reset_index()
        return summed_education_data
    
    def sum_all_state(self):
        summed_all_state_data = self.data.groupby(['Year', 'Education Level of Mother'])['Number of Births'].sum().reset_index()
        return summed_all_state_data

#Returns the current data.       
    def get_data(self):
        return self.data
    
#Filters and prints the matching states based on a keyword.

    def state_keyword_query(self, keyword):
        matching_states = [state for state in self.data['State'].unique() if keyword in state]
        print(f"Matching State for keyword '{keyword}':")
        for State in matching_states:
            print(State)

# Sorts the data by 'State' and 'Education Level of Mother',
# and aggregates the 'Number of Births' by sum and 'Average Age of Mother (years)' by mean.
# Returns the combined data.
    def sort_data(self):
        sorted_data = self.data.sort_values(by=['State', 'Education Level of Mother'])
        combined_data = sorted_data.groupby(['State', 'Year', 'Education Level of Mother']).agg({
            'Number of Births': 'sum',
            'Average Age of Mother (years)': lambda x: round(x.mean(), 1)
        }).reset_index()
        return combined_data

if __name__ == "__main__":
    file_path = 'Data/us_births_2016_2021.csv'       
    data_processor = US_Births(file_path)
    data_processor.read_csv()

    # remove columns
    columns_to_remove = ['State Abbreviation', 'Average Birth Weight (g)', 'Gender']  
    data_processor.remove_columns(columns_to_remove)
    
    #creates clean DataFrame
    cleaned_data = data_processor.get_data()
    cleaned_data.to_csv('Data/Cleaned_Births.csv', index=False)
    print("Cleaned data saved as 'Cleaned_Births.csv'.")

    keyword = 'keyword'  # Replace 'keyword' desired keyword
    data_processor.state_keyword_query(keyword)

    combined_data = data_processor.sort_data()
    combined_data.to_csv('Data/Avg_Mothers_Birth.csv', index=False)
    print("Cleaned data saved as 'Avg_Mothers_Birth.csv'.")

    summed_all_state_data = data_processor.sum_all_state()
    summed_all_state_data.to_csv('../Data/Sum_all_states.csv', index=False)
    print("Cleaned data saved as 'Summed All State'.")

     # Call the sum_births_by_year function to calculate the summed data by year and state
    for state in states:
        result_summed_data = data_processor.sum_births_by_year(state)

        # Save the summed data by year and state as "Summed.csv"
        result_summed_data.to_csv(f'../Data/Summed_{state}.csv', index=False)
        print(f"Summed data for {state} saved as 'Summed_{state}.csv'.")

    for state in states:
        result_summed_education_data = data_processor.sum_education_level(state)
        result_summed_education_data.to_csv(f'../Data/Summed_Education_Level_{state}.csv', index=False)
        print(f"Summed Education Level data for {state} saved as 'Summed_Education_Level_{state}.csv'.")