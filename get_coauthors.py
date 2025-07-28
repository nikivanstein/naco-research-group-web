# pip install google-search-results geopy

from serpapi import GoogleSearch
import os
import json

params = {
    "engine": "google_scholar_author",
    "author_id": "x7LEID0AAAAJ",
    "view_op": "list_colleagues",
    "api_key": os.getenv('SERP_API')
}

if False:
    search = GoogleSearch(params)
    results = search.get_dict()
    co_authors = results["co_authors"]

    js2 = json.dumps(co_authors, indent=4, sort_keys=True)
    fp2 = open('coauthors.json', 'w', encoding='utf-8')
    fp2.write(js2)


## Turn affiliations into geocoordinates
import json
from geopy.geocoders import Nominatim, GeocodeEarth, GoogleV3
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add a constant for the delay
GEOCODING_DELAY = 1  # 1 second delay

def get_coordinates(affiliation):
    """
    Retrieves the latitude and longitude for a given affiliation using the Nominatim geocoder.

    Args:
        affiliation (str): The affiliation string to geocode.

    Returns:
        tuple: A tuple containing (latitude, longitude) if successful, (None, None) otherwise.
    """
    geolocator_nominatim = Nominatim(user_agent="coauthor_location_app")
    geolocator_google = GoogleV3(api_key=os.getenv("GOOGLE_API"), user_agent="coauthor_location_app")

    max_retries = 3
    retry_delay = 5

    # Refine the affiliation string using regular expressions
    comma_index = affiliation.find(',')
    at_index = affiliation.find('@')

    if comma_index != -1 or at_index != -1:
        # Find the earlier of the two, if either exists
        if comma_index == -1:
            split_index = at_index
        elif at_index == -1:
            split_index = comma_index
        else:
            split_index = min(comma_index, at_index)
        affiliation = affiliation[split_index + 1:].strip()  # Take the part after the comma or @
    affiliation = affiliation.strip()

    for attempt in range(max_retries):
        try:
            location = geolocator_google.geocode(affiliation, timeout=10)
            if location:
                return location.latitude, location.longitude
        except GeocoderTimedOut:
            logging.warning(f"Nominatim timed out for: {affiliation}. Attempt {attempt + 1} of {max_retries}.")
            time.sleep(retry_delay)
        except GeocoderServiceError as e:
            logging.error(f"Nominatim service error for: {affiliation}: {e}")
            return None, None
        except Exception as e:
            logging.error(f"Nominatim error for {affiliation}: {e}")
            return None, None

    logging.error(f"Failed to geocode {affiliation} after {max_retries} attempts with both services.")
    return None, None

def process_coauthor_data(json_file_path):
    """
    Reads co-author data from a JSON file, geocodes the affiliations, and adds
    latitude and longitude information to each entry.

    Args:
        json_file_path (str): The path to the JSON file containing co-author data.

    Returns:
        list: A list of co-author dictionaries with added 'latitude' and 'longitude' keys.
                Returns an empty list on file errors.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error(f"Error: File not found at {json_file_path}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error: Invalid JSON in file {json_file_path}")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred while reading the JSON file: {e}")
        return []

    for entry in data:
        affiliation = entry.get('affiliations')  # Use .get() to handle missing affiliations
        if affiliation:
            latitude, longitude = get_coordinates(affiliation)
            entry['latitude'] = latitude
            entry['longitude'] = longitude
            time.sleep(1)  # Respectful delay to avoid overloading the service.  Important.
        else:
            logging.warning(f"Skipping entry because 'affiliations' field is missing: {entry}")
            entry['latitude'] = None
            entry['longitude'] = None

    return data

def save_enriched_data(data, output_file_path):
    """
    Saves the enriched co-author data (with latitude and longitude) to a new JSON file.

    Args:
        data (list): A list of co-author dictionaries with 'latitude' and 'longitude' keys.
        output_file_path (str): The path to the output JSON file.
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)  # Added ensure_ascii=False
        logging.info(f"Successfully saved enriched data to {output_file_path}")
    except Exception as e:
        logging.error(f"Error saving data to {output_file_path}: {e}")

if __name__ == "__main__":
    input_file_path = 'coauthors.json'  # Replace with the actual path to your JSON file
    output_file_path = 'coauthors_enriched.json' # Define output file name
    enriched_data = process_coauthor_data(input_file_path)
    if enriched_data:
        save_enriched_data(enriched_data, output_file_path)
    else:
        logging.info("No data to save.") #Handles the case where process_coauthor_data returns []
