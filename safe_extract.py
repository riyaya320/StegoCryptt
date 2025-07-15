#!/usr/bin/env python3
import sys
import zipfile
import pathlib

def extract_zip_safe(zip_path, extract_to='.'):
    """
    Safely extract zip file without relying on os.chmod
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files
            zip_ref.extractall(extract_to)
            print(f"Successfully extracted {zip_path} to {extract_to}")
            
            # List extracted files
            print("\nExtracted files:")
            for file_info in zip_ref.filelist:
                print(f"  {file_info.filename}")
                
    except FileNotFoundError:
        print(f"Error: {zip_path} not found")
        return False
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file")
        return False
    except Exception as e:
        print(f"Error extracting {zip_path}: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = extract_zip_safe("Crypto.zip")
    if success:
        print("\nExtraction completed successfully!")
    else:
        print("\nExtraction failed!")