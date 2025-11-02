import os


structure = {
    "sentiment-api": {
        "app": ["main.py", "model.py", "schemas.py", "__init__.py"],
        "tests": ["test_api.py"],
        ".github/workflows": ["ci-cd.yml"],
        ".": ["Dockerfile", "requirements.txt", "Makefile", "k6-load-test.js", "README.md"]
    }
}

def create_structure(base_path, structure):
    for root, contents in structure.items():
        root_path = os.path.join(base_path, root)
        for folder, files in contents.items():
            dir_path = os.path.join(root_path, folder)
            os.makedirs(dir_path, exist_ok=True)
            for file in files:
                file_path = os.path.join(dir_path, file)
                with open(file_path, 'w') as f:
                    f.write("")  # Empty file

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Project structure created successfully.")
