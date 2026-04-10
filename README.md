# SENG 3010 - Project Phase 4: Database Integration & Dynamic Content

## Project Overview
In Phase 4, we successfully transitioned the application from static/hardcoded data to a dynamic, containerized architecture. We implemented a PostgreSQL backend using Docker, allowing the Faculty and Course dashboards to pull real-time data through a CGI-enabled Apache web server.

## Key Accomplishments
* **Database Containerization:** Deployed a PostgreSQL database instance using **Docker**, ensuring a consistent environment for data storage.
* **Schema & Data Migration:** Successfully restored the `phase4_dashboard.dump` to populate the `faculty` and `courses` tables.
* **Backend Connectivity:** Refactored Python logic in `faculty.py` and `courses.py` to establish secure connections to the Postgres container.
* **Web Server Configuration:** Optimized the Apache environment by moving scripts to the `cgi-bin`, configuring execution permissions (`chmod +x`), and verified end-to-end data flow.
* **Troubleshooting:** Resolved initial "blank page" issues by debugging database socket connections and ensuring the DB container was fully initialized before web requests.

## Technical Stack
* **Backend:** Python (CGI)
* **Database:** PostgreSQL (running in Docker)
* **Web Server:** Apache
* **DevOps:** Docker


4.  **Access the Dashboards:**
    Navigate to the local or server URL for `faculty.py` or `courses.py` to view the live data.

## Status
**Phase 4 is fully functional.** The system correctly fetches and displays faculty and course data from the database end-to-end.
