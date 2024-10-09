import os

# Define the path to your docs folder
docs_folder = r'C:\Users\Huston\Documents\Portfolio\my-wiki\docs'

# Function to create index.md file and embed code files as markdown code blocks
def create_index(folder):
    index_file_path = os.path.join(folder, 'index.md')

    # Open (or create) index.md in write mode
    with open(index_file_path, 'w') as index_file:
        # Write the header
        folder_name = os.path.basename(folder).capitalize()
        index_file.write(f"# {folder_name}\n\n")
        index_file.write(f"Welcome to the {folder_name} section. Here are the available scripts:\n\n")

        # Loop through all files in the folder
        for file in os.listdir(folder):
            if file.endswith('.md') and file != 'index.md':  # Markdown files, excluding index.md
                index_file.write(f"- [{file.replace('.md', '')}]({file})\n")
            elif file.endswith('.py') or file.endswith('.sh'):  # Python or Bash files
                # Add the script file with a code block in Markdown
                index_file.write(f"\n## {file}\n\n")
                index_file.write("```" + ("python" if file.endswith('.py') else "bash") + "\n")

                # Read the script content
                with open(os.path.join(folder, file), 'r') as script_file:
                    index_file.write(script_file.read())

                index_file.write("\n```\n")

        print(f"Generated {index_file_path}")

# Loop through all folders in the docs directory
for folder in os.listdir(docs_folder):
    folder_path = os.path.join(docs_folder, folder)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        create_index(folder_path)
    else:
        print(f"{folder_path} is not a folder.")
