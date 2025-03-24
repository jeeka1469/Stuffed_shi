import os
from rich.console import Console
from rich.tree import Tree

console = Console()

def scan_repo(repo_path):
    """Scans the repository and returns a nested dictionary representing its structure."""
    file_map = {}
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.normpath(os.path.join(root, file))  # Normalize path
            relative_path = os.path.relpath(file_path, repo_path)
            file_map[relative_path] = file_path

    return file_map

def display_repo_tree(repo_path):
    """Displays the repository structure as a tree using rich."""
    repo_path = os.path.abspath(repo_path)  # Convert to absolute path

    if not os.path.exists(repo_path):
        console.print(f"❌ [red]Error: The path '{repo_path}' does not exist.[/red]")
        return

    if not os.path.isdir(repo_path):
        console.print(f"❌ [red]Error: '{repo_path}' is not a directory.[/red]")
        return

    file_map = scan_repo(repo_path)

    if not file_map:
        console.print(f"📁 [yellow]The repository '{repo_path}' is empty.[/yellow]")
        return

    tree = Tree(f"[bold cyan]{repo_path}[/bold cyan]")  # Root node
    nodes = {}

    for file in file_map.keys():
        parts = file.split(os.sep)
        parent = tree

        for i, part in enumerate(parts):
            path = os.sep.join(parts[:i + 1])

            if path not in nodes:
                if i == len(parts) - 1:  # It's a file
                    nodes[path] = parent.add(f"[blue]📄 {part}[/blue]")
                else:  # It's a folder
                    nodes[path] = parent.add(f"[green]📁 {part}[/green]")

            parent = nodes[path]

    console.print(tree)

if __name__ == "__main__":
    repo_path = input("Enter the path to your repository: ").strip()
    display_repo_tree(repo_path)