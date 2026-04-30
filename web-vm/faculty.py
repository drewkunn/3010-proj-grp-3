#!/usr/bin/env python3
import psycopg2
import cgi
import cgitb
import html as html_module

# Only enable cgitb in development — remove or guard this in production
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
        # Escape all values to prevent XSS
        return f"""
        <tr>
            <td>{html_module.escape(self.name or '')}</td>
            <td>{html_module.escape(self.rank or '')}</td>
            <td>{html_module.escape(self.email or '')}</td>
            <td>{html_module.escape(self.phone or '')}</td>
            <td>{html_module.escape(self.office or '')}</td>
            <td>{html_module.escape(self.research_interests or '')}</td>
            <td>{html_module.escape(self.remarks or '')}</td>
        </tr>
        """


RANK_ORDER = """
    ORDER BY
        CASE rank
            WHEN 'Professor' THEN 1
            WHEN 'Associate Professor' THEN 2
            WHEN 'Assistant Professor' THEN 3
            WHEN 'Administrative Assistant' THEN 4
            ELSE 5
        END,
        name
"""


def get_faculty_data(search=None):
    try:
        conn = psycopg2.connect(
            dbname="dashboard",
            user="webuser1",
            password="password",
            host="localhost",
            port=5432
        )
        cur = conn.cursor()

        if search:
            query = f"""
                SELECT id, name, rank, email, phone, office, research_interests, remarks
                FROM faculty
                WHERE name ILIKE %s OR rank ILIKE %s OR email ILIKE %s
                   OR phone ILIKE %s OR office ILIKE %s OR research_interests ILIKE %s
                   OR remarks ILIKE %s
                {RANK_ORDER};
            """
            param = f"%{search}%"
            cur.execute(query, (param,) * 7)
        else:
            cur.execute(f"""
                SELECT id, name, rank, email, phone, office, research_interests, remarks
                FROM faculty
                {RANK_ORDER};
            """)

        rows = cur.fetchall()
        faculty_list = [Faculty(*row) for row in rows]

        cur.close()
        conn.close()
        return faculty_list

    except Exception as e:
        print(f"<div style='color:red;border:2px solid red;padding:10px;'>"
              f"<b>Database Error:</b> {html_module.escape(str(e))}</div>")
        return []


def generate_html():
    form = cgi.FieldStorage()
    search = form.getvalue("search") or ""
    safe_search = html_module.escape(search)

    faculty_list = get_faculty_data(search if search else None)
    total = len(faculty_list)
    page_rows = faculty_list[:3]
    shown = len(page_rows)

    css = """
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background-color: white; color: #222; }

        .topbar { background-color: #2f80d1; color: white; padding: 10px 14px; font-size: 13px; }
        .topbar a { color: white; text-decoration: none; margin-right: 22px; }
        .title { font-weight: bold; margin-right: 18px; }
        .date-text { margin-right: 22px; }

        .container { padding: 8px 14px 20px 14px; }
        .section-tab {
            display: inline-block; padding: 8px 12px;
            border: 1px solid #d8d8d8; border-bottom: none;
            background-color: white; font-size: 12px; margin-bottom: 10px;
        }

        .toolbar { margin-bottom: 8px; font-size: 12px; }
        .toolbar select, .toolbar input { padding: 4px; border: 1px solid #d1d1d1; }
        .toolbar .right { float: right; }

        table { width: 100%; border-collapse: collapse; font-size: 12px; }
        th, td {
            border-top: 1px solid #e1e1e1; border-bottom: 1px solid #e1e1e1;
            padding: 8px 10px; text-align: left; vertical-align: top;
        }
        th { background-color: #fafafa; font-weight: bold; }

        .filter-row td { background-color: white; padding: 6px 8px; }
        .filter-row input, .filter-row select {
            width: 95%; box-sizing: border-box; padding: 6px;
            border: 1px solid #d6d6d6; background-color: white;
        }

        .bottom-controls {
            display: flex; justify-content: space-between; align-items: center;
            margin-top: 8px; font-size: 12px; color: #444;
        }
        .pagination span {
            display: inline-block; padding: 6px 10px;
            border: 1px solid #d0d0d0; margin-left: 4px; background: white;
        }
        .pagination .active { background: #f0f0f0; }
    </style>
    """

    rows_html = "".join(f.to_html() for f in page_rows)

    return f"""
    <html>
    <head><title>ECU CS Dashboard - Faculty</title>{css}</head>
    <body>

    <div class="topbar">
        <span class="title">ECU CS Dashboard</span>
        <span class="date-text">29 March 2021</span>
        <a href="/cgi-bin/faculty.py">Faculty</a>
        <a href="/cgi-bin/courses.py">Courses</a>
        <a href="#">SCH Drilldown</a>
        <a href="#">FTE</a>
        <a href="#">Faculty Committees</a>
        <a href="#">Resources</a>
    </div>

    <div class="container">
        <div class="section-tab">Faculty</div>

        <div class="toolbar">
            Show <select><option>3</option></select> entries
            <span class="right">
                <form method="GET" style="display:inline;">
                    Filter <input type="text" name="search" value="{safe_search}">
                </form>
            </span>
        </div>

        <table>
            <tr>
                <th>Name</th><th>Rank</th><th>Email</th><th>Phone</th>
                <th>Office</th><th>Research Interests</th><th>Remarks</th>
            </tr>
            <tr class="filter-row">
                <td><input type="text"></td>
                <td><input type="text"></td>
                <td><select><option>All</option></select></td>
                <td><input type="text"></td>
                <td><input type="text"></td>
                <td><select><option>All</option></select></td>
                <td><input type="text"></td>
            </tr>
            {rows_html}
        </table>

        <div class="bottom-controls">
            <div>Showing 1 to {shown} of {total} entries</div>
            <div class="pagination">
                <span>Previous</span>
                <span class="active">1</span>
                <span>2</span>
                <span>3</span>
                <span>Next</span>
            </div>
        </div>
    </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    print(generate_html())
