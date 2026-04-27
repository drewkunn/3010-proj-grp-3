# SENG3010 Project - Phase 4B: Dashboard Containerization & FTE Migration

## Project Overview
[cite_start]This phase focused on "future-proofing" the faculty dashboard by migrating the database architecture from a standalone VirtualBox VM to a containerized environment running on the Web-VM[cite: 17, 18]. [cite_start]The goal was to achieve full independence, allowing the web application to function without the original PGSQL or Main VMs[cite: 21].

## VM File Locations
All project components are stored on the **Websrv-VM** in the following directories:

* [cite_start]**Project Root**: `~/3010-proj-grp-3/` (This is the main folder containing all phase 4 files)[cite: 45].
* [cite_start]**Database Backup**: `~/3010-proj-grp-3/DB/dbsrv-bak-pg-dumpall.sql` (The SQL dump used for the migration)[cite: 41].
* [cite_start]**Web Content**: `~/3010-proj-grp-3/webpages/` (Contains the dashboard UI and `fte.py` logic)[cite: 42].
* [cite_start]**Docker Config**: `~/3010-proj-grp-3/Dockerfile` (The script used to build the PostgreSQL container)[cite: 31].
* **Live Web Directory**: `/var/www/html/` (The system location where Apache serves the site).

## Part 1: Containerization & Infrastructure
In the first half, we established the core infrastructure required for containerization:

* [cite_start]**Custom Dockerfile**: Developed a `Dockerfile` that builds an image from scratch using the official Ubuntu 24.04 base[cite: 22, 23].
* [cite_start]**Automated Installation**: Used `APT` commands within the Dockerfile to install the latest PostgreSQL version, avoiding pre-built database images as required[cite: 32].
* [cite_start]**Service Automation**: Configured the container to start automatically upon Web-VM boot, ensuring the PostgreSQL service is always ready to handle queries[cite: 19].
* [cite_start]**Web Server Integration**: Verified that Apache starts automatically on the Web-VM to serve the dashboard interface[cite: 20].

## Part 2: Data Migration & FTE Implementation
The second half involved restoring project data and adding new analytical features:

* **Database Migration**: 
    * [cite_start]Exported the original database structure and data using `pg_dumpall`[cite: 9, 41].
    * Successfully restored this backup into the new Docker container (`pg-db`), verified by the presence of the `faculty` table and associated relations.
* **FTE Feature**: 
    * [cite_start]Implemented a new **FTE (Full-Time Equivalent)** tab on the dashboard[cite: 28, 44].
    * [cite_start]Developed Python objects and methods within `webpages/fte.py` to calculate and display faculty FTE values based on database records[cite: 7, 29].
* **Independence Verification**: 
    * [cite_start]Confirmed the Web-VM's self-sufficiency by powering off the Main-VM and original PGSQL-VM[cite: 5, 21].
    * [cite_start]Verified that the dashboard and FTE calculations remain fully functional, pulling data exclusively from the local Docker container[cite: 21].

## Submission Details
* [cite_start]**Project Branch**: All files are maintained in the `phase4` branch of the GitHub repository[cite: 40].
* [cite_start]**Archive**: The full project directory has been compressed into `phase4_final.tar` for submission[cite: 45].
