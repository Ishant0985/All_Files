import os

def delete_file(filepath):
    try:
        # Check if the file exists
        if os.path.exists(filepath):
            # Delete the file
            os.remove(filepath)
            print(f"File '{filepath}' has been deleted successfully.")
        else:
            print(f"File '{filepath}' does not exist.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")

if __name__ == "__main__":
    filepath = r"C:\Users\scien\OneDrive\Documents\.pieces_identities"
    delete_file(filepath)
