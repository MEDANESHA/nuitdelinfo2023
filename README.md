# nuitdelinfo2023
# My Project

This repository contains the source code for my project. The project uses GitHub Actions to automatically extract code from a Docker image and push it to the GitHub repository. Below is a brief overview of the workflow.

## GitHub Actions Workflow: Extract Code and Deploy

### Trigger

The workflow is triggered on each push to the `main` branch.

### Workflow Steps

1. **Checkout Repository:**
   - Uses GitHub Actions' `checkout` action to clone the repository.

2. **Extract Code from Docker Image:**
   - Runs a Docker container (`medanes/retroverse_pipeline:latest`) to extract code from the `/app/` directory.
   - Creates a local directory `extracted-code` and copies extracted code into it.

3. **Configure Git and Commit Changes:**
   - Initializes a new Git repository within the `extracted-code` directory.
   - Configures Git user email and name.
   - Adds all changes to the staging area.
   - Commits the changes with a commit message indicating the extraction.

4. **Pull Latest Changes from Remote `main` Branch:**
   - Fetches the latest changes from the remote `main` branch.
   - Creates a new local branch (`main`) and checks it out.
   - Pulls the latest changes from the remote `main` branch into the local branch.

5. **Push Extracted Code to GitHub:**
   - Adds the GitHub repository as a remote (`origin`) with authentication using GitHub Actions' secrets.
   - Pushes the changes to the `main` branch on the GitHub repository.
 
### GitHub Actions Settings

- **Workflow Permissions:**
  - The GitHub Actions workflow has read and write permissions.
  
- **Pull Request Permissions:**
  - GitHub Actions is allowed to create and approve pull requests.

### Additional Notes

- The `.git` directory is removed from the extracted code to avoid overwriting existing repository data.
- This workflow is designed to be triggered automatically on each push to the `main` branch.

### Author

- Your EPI_CODING_AVENGERS
- Your mouhamed195h@gmail.com

