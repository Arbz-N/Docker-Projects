# Docker-Based Folder Backup Tool

This project provides a **simple and automated folder backup solution** using **Docker**.  
It uses a lightweight **Alpine Linux container** to copy files from a source directory to a timestamped backup directory on the host machine.  
The project also demonstrates how to automate backups using **cron jobs**.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Project Structure](#project-structure)  
- [Dockerfile Explanation](#dockerfile-explanation)  
- [Backup Script (`script.sh`) Explanation](#backup-script-scriptsh-explanation)  
- [Setup and Usage](#setup-and-usage)  
- [Cron Job Integration](#cron-job-integration)  
- [Output Example](#output-example)  


---

## Project Overview

The project performs the following tasks:

1. Builds a **Docker image** based on Alpine Linux.  
2. Creates `/source` and `/backup` directories inside the container.  
3. Copies all files from the host source directory to a timestamped backup directory.  
4. Optionally, automates backup execution using **cron jobs**.

---

## Project Structure

```bash
.
- Dockerfile        # Docker image definition
- script.sh         # Backup automation script
- README.md         # Project documentation
Dockerfile Explanation
dockerfile
FROM alpine:latest

RUN mkdir /source /backup
WORKDIR /source
CMD cp -r /source/* /backup/
What this does:
Base image: Alpine Linux for minimal size and fast execution

Directories:

/source → Container mount for the source folder
/backup → Container mount for backup storage

Default command: Copies all files from /source to /backup when the container runs

Backup Script (script.sh) Explanation

#!/bin/bash

source_directory="/path/to/source-folder" #Source directory on host
backup_directory="/path/to/backup-directory" #Base backup directory on host
backup_image="backup_tool:latest" # Docker image name
timestamp=$(date +"%Y-%m-%d_%H-%M-%S") # Timestamp for unique backups
backup_volume="$backup_directory/folder-${timestamp}" # Backup folder for this run

perform_backup() {
    docker run --rm \
        -v "$source_directory:/source" \  #Mounts host source folder to container /source
        -v "$backup_volume:/backup" \     #Mounts backup folder to container /backup
        "$backup_image"
}

main() {
    echo "Starting folder backup..."

    perform_backup

    echo "Backup completed successfully!"
    echo "Backup stored at: $backup_volume"
}

main  #to call main function

Setup and Usage
1. Build the Docker Image

docker build -t backup_tool:latest .

2. Make Script Executable

chmod +x script.sh
3. Run Backup Script

./script.sh

Cron Job Integration (Automated Backups)
To schedule the backup script to run automatically:

Open the cron editor:

crontab -e
Add a line to run backup daily at 2 AM:

bash
Copy code
0 2 * * * /bin/bash /path/to/script.sh >> /path/to/backup_log.log 2>&1

Explanation:

0 2 * * * → Runs at 2:00 AM every day

>> /path/to/backup_log.log 2>&1 → Appends stdout and stderr to log file
Replace /path/to/script.sh with the absolute path to your script

Save and exit the editor.
The script will now run automatically at the scheduled time.

Output Example

Starting folder backup...
Backup completed successfully!
Backup stored at: /path/to/backup-directory/folder-2025-12-21_23-45-12