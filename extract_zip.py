import zipfile
import os
import sys

def extract_crypto_zip():
    zip_path = 'Crypto.zip'
    extract_dir = 'extracted_crypto'
    
    if not os.path.exists(zip_path):
        print(f"Error: {zip_path} not found in current directory")
        return False
    
    try:
        # Create extraction directory
        os.makedirs(extract_dir, exist_ok=True)
        
        # Extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            
        print(f"Successfully extracted {zip_path} to {extract_dir}/")
        
        # List all extracted files
        print("\nExtracted files and directories:")
        for root, dirs, files in os.walk(extract_dir):
            level = root.replace(extract_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}📁 {os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}📄 {file}")
                
        return True
        
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file")
        return False
    except Exception as e:
        print(f"Error extracting zip file: {str(e)}")
        return False

if __name__ == "__main__":
    success = extract_crypto_zip()
    if not success:
        sys.exit(1)