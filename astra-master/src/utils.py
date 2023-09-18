import requests
import zipfile


def download_file() -> None:
    """ download zip from given url """
    url = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"
    target_file = "../raw_data/astra.zip"

    try:
        resp = requests.get(url)
        resp.raise_for_status()
        with open(target_file, "wb") as f:
            f.write(resp.content)
        print(f"File downloaded successfully to {target_file}")
    except requests.exceptions.RequestException as ex:
        print(f"Failed to download the file. Error {resp.status_code}")


def unzip_file() -> None:
    """ unzip file on given path """
    filepath = "../raw_data/astra.zip"
    target_dir = "../raw_data/"

    try:
        with zipfile.ZipFile(filepath, "r") as zip_ref:
            zip_ref.extractall(target_dir)
        print(f"File {filepath} extracted to {target_dir}")
    except FileNotFoundError:
        print(f"Error: The file {filepath} does not exist.")
    except zipfile.BadZipFile:
        print(f"Error: {filepath} is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

