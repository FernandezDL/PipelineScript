# PipelineScript
Pipeline Script for the Pipelines Class at VFS

## Description
This project consist on creating a simple pipeline designated to validate the health of the assets in a game development environment. The pipeline scans a directory of files, checks for common issues, and generates a report with warnings and errors and have been detected with the assets.

The goal of the pipeline is to ensure the consistency on all the assets names and prevent problematic files from being used in the project, also allowing the projecto to grow in an orderly and controlled way.

## Features
The pipeline performs the following validations:
- Detects any empty directories
- Detects duplicated files across all folders in the main directory
- Validate file names:
   - Replaces spaces with _ to create `snake_case` file names
   - Replaces special characters like `ñ` to help spanish writers
- Checks file sizes:
   - File bigger than 5M: Generates `warning`
   - File bigger than 20M: Generates `error`
- Generates a structured report with the results
   - The reports are created in a `Reports` folder and get added the time and date of the creation of wach file.

## Project structure
│

├── assets/ # Folder containing files to validate

├── reports/ # Generated reports

├── checker.py # Main pipeline script

└── run_pipeline.cmd # File that executes the Main pipeline script

## Run
1. Download the project
2. Ensure to have the same project structure as shown previously
3. Place the files to check inside the `assets` folder (this project has a few examples)
4. To run the pipeline open a `CMD` terminal and run the command
```code
run_pipeline.cmd
```

## Author
Diana Lucia Fernandez Villatoro
PG29
