def process_file(file_path, limit=None):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        if limit is not None:
            lines = lines[:limit]
        
        # Process the lines here
        # ...
