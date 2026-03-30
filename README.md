# SENG 3010 - Project Phase 3: Faculty Dashboard
**Team 3**

## 📌 Project Overview
This phase focused on transitioning our application into a professional, organized structure while implementing the core logic for the Faculty Dashboard. We have successfully separated the frontend UI from the backend logic and established a relational database structure.

---

## 📂 Project Structure & Organization
To meet the rubric requirements for organization, the repository has been restructured:

* **/webpages**: Contains all CGI Python scripts (`.py`) and HTML templates (`.html`).
    * `faculty.html`: The main Dashboard UI featuring the global navigation bar.
    * `faculty.py`: Logic for searching and displaying faculty data.
    * `courses.py`: Logic for displaying the course list using Object-Oriented programming.
* **/DB**: Contains database infrastructure and backups.
    * `team3_db_backup.sql`: A full `pg_dumpall` backup of the project database.
* **README.md**: Documentation of the project state and structure.

---

## 🛠 Features Implemented

### 1. Global Navigation & UI
* Implemented a **Global Navigation Bar** (Blue Header) across all dashboard pages to allow seamless switching between Faculty, Courses, FTE, SCH, Committees, and Resources.
* Ensured consistent styling across the dashboard for a professional user experience.

### 2. Object-Oriented Logic (Requirement: Item 8)
* Created a **`Course` Class** in `courses.py` to handle data mapping. 
* Database rows are fetched and instantiated as Python objects before being rendered to the HTML table, fulfilling the requirement for OO logic in the application layer.

### 3. Relational Database Expansion
* Created new relational tables for **Faculty Committees** and **Resources**.
* Populated the database with initial data to verify successful connection and retrieval via the web interface.

### 4. Git & DevOps
* Managed version control via a dedicated `phase3` branch.
* Implemented secure pushing via GitHub **Personal Access Tokens (PAT)** to resolve authentication constraints.

---

## 🚀 How to Run
1.  Navigate to the project directory: `cd ~/3010-proj-grp-3`
2.  Ensure permissions are set: `chmod -R 755 webpages/`
3.  Access the dashboard via: `localhost/webpages/faculty.html`
