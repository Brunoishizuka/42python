import sys
import hashlib

def calculate_geohash(latitude, longitude):
    # Convert latitude and longitude to strings with 12 decimal places
    lat_str = '{:.12f}'.format(latitude)
    lon_str = '{:.12f}'.format(longitude)

    # Concatenate latitude and longitude strings with a comma separator
    coordinates_str = "{},{}".format(lat_str, lon_str)

    # Use hashlib to calculate MD5 hash of the concatenated coordinates
    hash_object = hashlib.md5(coordinates_str.encode())

    # Get the hexadecimal representation of the hash and truncate it to 10 characters
    geohash = hash_object.hexdigest()[:10]

    return geohash

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python geohashing.py <latitude> <longitude>")
        sys.exit(1)

    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])

    try:
        # Calculate geohash
        geohash = calculate_geohash(latitude, longitude)

        # Display the geohash
        print("Geohash:", geohash)

    except Exception as e:
        # Display error message
        print("An error occurred:", e)
