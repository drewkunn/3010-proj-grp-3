# SENG3010 Team 3 - Main Project

# Phase 3 Project - Course Information Module

## Overview


## Jarmaine's Contributions

### 1. Object-Oriented Python Development (courses.py)
In accordance with the Phase 3 requirements for Object-Oriented Programming (OOP), I developed the `courses.py` script.
* **Class Structure**: Created a `CourseDisplay` class to encapsulate the webpage logic.
* **Methods**: Implemented methods to handle CGI form data and output the required HTML for the Course Info section.
* **CGI Integration**: Configured the script to interact with the web server, ensuring proper Content-Type headers and HTML formatting for browser display.

### 2. Database Management & Security
* **Data Persistence**: Performed a `pg_dumpall` on the PostgreSQL database to create a full backup of the current schema and data.
* **Directory Organization**: Created a dedicated `/DB` directory at the root of the project and moved the SQL dump into it to ensure it is version-controlled and easily recoverable.

### 3. Deployment & Packaging
* **File Structure**: Organized all web-facing Python scripts and configuration files into the `/webpages` directory.
* **Tarball Creation**: Generated the `team3_phase3.tar` submission file from the main project directory, ensuring all team contributions and configuration files were included for the professor.
* **Validation**: Verified the integrity of the archive using the `tar -tvf` command to confirm all paths and files were correctly mapped.

## VM & Environment State
* **Snapshot**: A final snapshot of the VM (labeled "Phase 3 Final") was taken in a "Powered Off" state to meet the specific requirements for the vCloud Director environment.
