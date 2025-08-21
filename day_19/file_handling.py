import json
from collections import Counter
import os

def read_countries_data(file_path='data/countries_data.json'):
    """
    Read countries data from JSON file
    
    Args:
        file_path (str): Path to the JSON file. Defaults to 'data/countries_data.json'
    
    Returns:
        list: List of country dictionaries or None if error occurs
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            # Try alternative paths
            alternative_paths = [
                '../data/countries.json',
                './countries.json',
                'countries.json'
            ]
            
            for alt_path in alternative_paths:
                if os.path.exists(alt_path):
                    file_path = alt_path
                    break
            else:
                raise FileNotFoundError(f"Could not find countries_data.json in any expected location")
        
        # Read and parse the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            countries_data = json.load(file)
        
        print(f"Successfully loaded data for {len(countries_data)} countries")
        return countries_data
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def find_top_ten_languages(countries_data, top_nums):
    """
    Find the ten most spoken languages from countries data
    
    Args:
        countries_data (list): List of country dictionaries
    
    Returns:
        list: List of tuples containing (language, count) for top 10 languages
    """
    if not countries_data:
        return []
    
    # Count occurrences of each language
    language_counter = Counter()
    
    for country in countries_data:
        # Get languages list for current country
        languages = country.get('languages', [])
        # Some data might have languages as a list, others might have different formats
        if isinstance(languages, list):
            language_counter.update(languages)
        elif isinstance(languages, str):
            # Handle case where languages might be a comma-separated string
            lang_list = [lang.strip() for lang in languages.split(',')]
            language_counter.update(lang_list)
    
    # Get top 10 languages
    top = language_counter.most_common(top_nums)
    print(top)
    return top

def find_most_populated(countries_data, num_countries):
	if not countries_data:
	    return []

	population_data = []
	for country in countries_data:
	    country_name = country.get('name', 'Unknown')
	    # Handle different possible population field names
	    population = country.get('population') or country.get('Population') or 0
	    
	    # Ensure population is an integer
	    if isinstance(population, str):
	        try:
	            population = int(population.replace(',', ''))
	        except ValueError:
	            population = 0
	    elif not isinstance(population, int):
	        population = 0
	        
	    population_data.append({
	        'country': country_name,
	        'population': population
	    })

	# Sort by population in descending order
	population_data.sort(key=lambda x: x['population'], reverse=True)
	# print(population_data)

	# Return top N countries
	return population_data[:num_countries]


def main():
    """Main function to demonstrate the solution"""
    # Read the data
    print("Reading countries data...")
    countries_data = read_countries_data()
    
    if not countries_data:
        print("Failed to read countries data. Please check the file path.")
        return
    
    # Option 1: Simple top 10 languages
    print("\n=== Top 10 Most Spoken Languages ===")
    top_languages = find_top_ten_languages(countries_data, 5)
    most_populated = find_most_populated(countries_data, 5)
    
    for rank, (language, count) in enumerate(top_languages, 1):
        print(f"{rank:2d}. {language}: {count} countries")

    print("\nTop 10 Most Populated Countries:")
    print("[")
    for country in most_populated:
        print(f"{{'country': '{country['country']}', 'population': {country['population']}}},")
    print("]")

# Example usage
if __name__ == "__main__":
    main()
    
    # Additional: If you want to export results to a file
    # countries_data = read_countries_data()
    # if countries_data:
    #     export_results_to_file(countries_data)