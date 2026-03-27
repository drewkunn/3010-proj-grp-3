# Phase 3 Project Submission - Team 3

## Project Overview
This project is a functional ECU CS Dashboard. It utilizes a PostgreSQL backend on a dedicated DB server (`dbsrv`) and a Python-CGI frontend on a Web server (`websrv`).



### 1. Database & Infrastructure (Directory: `/DB`)
* **File: `team3_db_backup.sql`** - I performed a full system `pg_dumpall` to ensure all data is preserved.
* **Tables Created:** I manually built the relational structures for `faculty_committees` and `recources`.
* **Environment:** Verified connectivity between the web and database virtual machines.

### 2. Web Development (Directory: `/webpages`)
* **File: `faculty.html`** - I developed the main Dashboard UI.
* **Global Navigation:** I hand-coded the blue "ECU CS Dashboard" header with links for:
  - Faculty (`faculty.py`)
  - Courses (`courses.py`)
  - SCH Drilldown, FTE, Committees, and Resources (Placeholders).
* **Object-Oriented Logic:** Implemented the Python `Course` class and methods to pull and display data dynamically from the database.

### 3. Submission Packaging
* **File: `team3_phase3.tar`** - I organized the final directory structure and compressed the project for Canvas submission.
* **Snapshot:** A clean system state was saved as "Phase 3 Final" in vCloud.

## How to Run
1. Ensure the PostgreSQL service is running on the DB server.
2. Open Firefox in the Web VM and navigate to `localhost/webpages/faculty.py`.
