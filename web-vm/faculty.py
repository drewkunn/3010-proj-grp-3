#!/usr/bin/python3
import psycopg2
import cgi
import cgitb
import sys

# ENABLE DEBUGGING: This makes the browser show the specific Python error
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
        # Matches your exact <tr> structure from the screenshots
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
        # FIXED: Connecting to 'facultdb' on localhost (Docker port mapping)
        conn = psycopg2.connect(
            dbname="facultdb",
            user="postgres",
            host="localhost",
            port=5432
        )
        cur = conn.cursor()

        if search:
            # Full search logic across all columns as seen in your code
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
        # Ultimate Debugging: Prints the DB error inside a clean box on the web page
        print(f"<div style='background:white; color:red; border:2px solid red; padding:10px;'>")
        print(f"<b>Database Error:</b> {e}</div>")
        return []

def generate_html():
    form = cgi.FieldStorage()
    search = form.getvalue("search")
    faculty_list = get_faculty_data(search)

    # Rebuilding your CSS exactly from the screenshots
    css = """
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background-color: white; color: #222; }
        .topbar { background-color: #2f80d1; color: white; padding: 10px 14px; font-size: 13px; }
        .topbar a { color: white; text-decoration: none; margin-right: 22px; }
        .title { font-weight: bold; margin-right: 18px; }
        .container { padding: 8px 14px 20px 14px; }
        .section-tab { 
            display: inline-block; padding: 8px 12px; border: 1px solid #d8d8d8; 
            border-bottom: none; background-color: white; font-size: 12px; margin-bottom: 10px; 
        }
        .toolbar { margin-bottom: 8px; font-size: 12px; }
        .toolbar select, .toolbar input { padding: 4px; border: 1px solid #d1d1d1; }
        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th { text-align: left; background-color: #f2f2f2; border: 1px solid #ccc; padding: 6px; }
        td { border: 1px solid #ccc; padding: 6px; }
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
            <span class="title">ECU CS Dashboard</span>
            <a href="#">Faculty</a>
            <a href="#">Courses</a>
            <a href="#">Resources</a>
        </div>
        <div class="container">
            <div class="section-tab">Faculty List</div>
            <div class="toolbar">
                <form method="get">
                    <input type="text" name="search" placeholder="Search faculty..." value="{search if search else ''}">
                    <input type="submit" value="Search">
                    <span style="margin-left:20px;">Showing {len(faculty_list)} Faculty Members</span>
                </form>
            </div>
            <table>
                <tr>
                    <th>Name</th><th>Rank</th><th>Email</th><th>Phone</th><th>Office</th><th>Interests</th><th>Remarks</th>
                </tr>
                {"".join([f.to_html() for f in faculty_list])}
            </table>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    print(generate_html())
