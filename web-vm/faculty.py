#!/usr/bin/python3
import psycopg2
import cgi
import cgitb
import sys

# ENABLE DEBUGGING
cgitb.enable()

print("Content-Type: text/html\n")

class Faculty:
    def __init__(self, faculty_id, name, rank, email, phone, office, research_interests, remarks):
        self.faculty_id = faculty_id
        self.name = name
        self.rank = rank
        self.email = email
        self.phone = phone
        self.office = office
        self.research_interests = research_interests
        self.remarks = remarks

    def to_html(self):
        return f"""
        <tr>
            <td>{self.name}</td>
            <td>{self.rank}</td>
            <td>{self.email}</td>
            <td>{self.phone}</td>
            <td>{self.office}</td>
            <td>{self.research_interests}</td>
            <td>{self.remarks}</td>
        </tr>
        """

def get_faculty_data(search=None):
    try:
        # UPDATED: Connecting to 'dashboard' as 'webuser1'
        conn = psycopg2.connect(
            dbname="dashboard",
            user="webuser1",
            password="password",
            host="localhost",
            port=5432
        )
        cur = conn.cursor()

        if search:
            query = """
                SELECT id, name, rank, email, phone, office, research_intrests, remarks 
                FROM faculty 
                WHERE name ILIKE %s OR rank ILIKE %s OR email ILIKE %s 
                   OR phone ILIKE %s OR office ILIKE %s OR research_intrests ILIKE %s 
                   OR remarks ILIKE %s
                ORDER BY 
                    CASE rank 
                        WHEN 'Professor' THEN 1 
                        WHEN 'Associate Professor' THEN 2 
                        WHEN 'Assistant Professor' THEN 3 
                        ELSE 4 END, 
                    name;"""
            search_param = f"%{search}%"
            cur.execute(query, (search_param,) * 7)
        else:
            cur.execute("SELECT id, name, rank, email, phone, office, research_intrests, remarks FROM faculty ORDER BY id ASC;")

        rows = cur.fetchall()
        faculty_list = [Faculty(*row) for row in rows]
        
        cur.close()
        conn.close()
        return faculty_list
    except Exception as e:
        print(f"<div style='background:white; color:red; border:2px solid red; padding:10px;'>")
        print(f"<b>Database Error:</b> {e}</div>")
        return []

def generate_html():
    form = cgi.FieldStorage()
    search = form.getvalue("search")
    faculty_list = get_faculty_data(search)

    # NEW: Professional CSS to match the main VM screenshot
    css = """
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background-color: #f4f7f6; color: #333; }
        .topbar { background-color: #4a90e2; color: white; padding: 10px 20px; display: flex; align-items: center; font-size: 14px; }
        .topbar .brand { font-weight: bold; margin-right: 25px; font-size: 16px; }
        .topbar a { color: rgba(255,255,255,0.8); text-decoration: none; margin-right: 20px; }
        
        .container { padding: 20px; }
        .card { background: white; border: 1px solid #dee2e6; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        
        .tab-btn { display: inline-block; padding: 8px 15px; border: 1px solid #dee2e6; border-bottom: none; background: #fff; font-size: 13px; border-radius: 4px 4px 0 0; margin-left: 2px; }
        
        .toolbar { padding: 15px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; border-bottom: 1px solid #eee; }
        .toolbar input { padding: 5px; border: 1px solid #ccc; border-radius: 3px; }

        table { width: 100%; border-collapse: collapse; background: white; }
        th { background-color: #f8f9fa; color: #444; font-weight: 600; padding: 10px; text-align: left; border: 1px solid #dee2e6; font-size: 13px; }
        td { padding: 10px; border: 1px solid #dee2e6; font-size: 13px; }
        
        .filter-row input { width: 90%; padding: 3px; font-size: 11px; border: 1px solid #ddd; }
        .pagination-info { padding: 15px; font-size: 13px; color: #666; display: flex; justify-content: space-between; }
    </style>
    """

    html_content = f"""
    <html>
    <head>
        <title>ECU CS Dashboard - Faculty</title>
        {css}
    </head>
    <body>
        <div class="topbar">
            <span class="brand">ECU CS Dashboard</span>
            <span style="color:rgba(255,255,255,0.5); margin-right:20px;">29 March 2021</span>
            <a href="#">Faculty</a> <a href="#">Courses</a> <a href="#">Resources</a>
        </div>
        <div class="container">
            <div class="tab-btn">Faculty</div>
            <div class="card">
                <div class="toolbar">
                    <div>Show <select><option>3</option></select> entries</div>
                    <form method="get" style="margin:0;">
                        Filter: <input type="text" name="search" value="{search if search else ''}">
                    </form>
                </div>
                <table>
                    <tr>
                        <th>Name</th><th>Rank</th><th>Email</th><th>Phone</th><th>Office</th><th>Interests</th><th>Remarks</th>
                    </tr>
                    <tr class="filter-row">
                        <td><input type="text"></td><td><input type="text"></td><td><input type="text"></td>
                        <td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td>
                    </tr>
                    {"".join([f.to_html() for f in faculty_list])}
                </table>
                <div class="pagination-info">
                    <div>Showing 1 to {len(faculty_list)} of {len(faculty_list)} entries</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    print(generate_html())
