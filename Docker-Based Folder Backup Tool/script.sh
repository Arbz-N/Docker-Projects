#!/bin/bash

source_directory="/home/ubuntu/folder"
backup_directory="/home/ubuntu/backup_data"
backup_image="backup_tool:latest"
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
backup_volume="$backup_directory/folder-${timestamp}"




perform_backup() {

        docker run --rm \
                -v "$source_directory:/source" \
                -v "$backup_volume:/backup" \
                "$backup_image"
}

main() {
        echo "Starting Folder backup....."

        perform_backup
        echo "✅ Backup completed successfully!"
        echo "📦 Backup stored at: $backup_directory/$timestamp"
}

main


