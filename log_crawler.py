import os
import logging
import argparse

# Basic logging setup:
logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Argument parser setup:
def set_search_variables():
    parser = argparse.ArgumentParser(description="Search files in a directory for a specific term. \
                                     The search is not case sensitive by default.")
    parser.add_argument("search_term", help="Term to search for in the files.")
    parser.add_argument("file_ext", help="File extension to search within (e.g. txt, log).")
    parser.add_argument("directory", help="Directory to start the search from.")
    parser.add_argument("-c", "--case-sensitive", action="store_true", help="Make the search case-sensitive.")

    args = parser.parse_args()

    # Add dot prefix to file extension if missing
    if not args.file_ext.startswith("."):
        logging.info("Adding . to file extension")
        args.file_ext = "." + args.file_ext

    logging.info("Crawling directory: %s", args.directory)
    logging.info("Case sensitive: %s", args.case_sensitive)
    
    return args.search_term, args.file_ext, args.directory, args.case_sensitive

def search_directory(directory, search_term, file_ext):
    result_count = 0
    logging.info("Searching for term: %s in files with extension: %s",
                    search_term, file_ext)
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith(file_ext):
                full_file_path = os.path.join(dirpath, file)
                logging.info(f"Found file: {full_file_path}")
                try:
                    with open(full_file_path, "r") as f:
                        line_count = 0
                        for line in f:
                            line_count += 1
                            if case_sensitive:  # If case sensitive is True
                                if search_term in line:
                                    result_count += 1
                                    logging.info(f"{result_count} - Found search term: \"{search_term}\" on line:\n{line_count} - {line.strip()}")
                                    
                            else:  # If case sensitive is False
                                if search_term.lower() in line.lower():  # Convert both to lowercase and search
                                    result_count += 1
                                    logging.info(f"{result_count} - Found search term: \"{search_term}\" on line:\n{line_count} - {line.strip()}")

                    logging.info("Found %s results", result_count)
                except Exception as e:
                    logging.error("Error opening file: %s", e)


search_term, file_ext, crawl_directory, case_sensitive = set_search_variables()
search_directory(crawl_directory, search_term, file_ext)
