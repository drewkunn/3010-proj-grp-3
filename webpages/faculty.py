#!/usr/bin/env python3
import psycopg2
import cgi


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
    conn = psycopg2.connect(
        dbname="dashboard",
        user="webuser1",
        password="password",
        host="localhost"
    )

    cur = conn.cursor()

    if search:
        cur.execute("""
        SELECT * FROM faculty
        WHERE name ILIKE %s
           OR rank ILIKE %s
           OR email ILIKE %s
           OR phone ILIKE %s
           OR office ILIKE %s
           OR research_interests ILIKE %s
           OR remarks ILIKE %s
        ORDER BY
            CASE rank
                WHEN 'Professor' THEN 1
                WHEN 'Associate Professor' THEN 2
                WHEN 'Assistant Professor' THEN 3
                WHEN 'Administrative Assistant' THEN 4
                ELSE 5
            END,
            name;
        """, (
            '%' + search + '%',
            '%' + search + '%',
            '%' + search + '%',
            '%' + search + '%',
            '%' + search + '%',
            '%' + search + '%',
            '%' + search + '%'
        ))
    else:
        cur.execute("""
        SELECT * FROM faculty
        ORDER BY
            CASE rank
                WHEN 'Professor' THEN 1
                WHEN 'Associate Professor' THEN 2
                WHEN 'Assistant Professor' THEN 3
                WHEN 'Administrative Assistant' THEN 4
                ELSE 5
            END,
            name;
        """)

    rows = cur.fetchall()
    faculty_list = []

    for row in rows:
        f = Faculty(
            row[0],  # id
            row[1],  # name
            row[2],  # rank
            row[3],  # email
            row[4],  # phone
            row[5],  # office
            row[6],  # research_interests
            row[7]   # remarks
        )
        faculty_list.append(f)

    cur.close()
    conn.close()
    return faculty_list


def generate_html():
    form = cgi.FieldStorage()
    search = form.getvalue("search")

    faculty_list = get_faculty_data(search)
    shown_rows = min(len(faculty_list), 3)

    html = """
    <html>
    <head>
        <title>ECU CS Dashboard - Faculty</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: white;
                color: #222;
            }

            .topbar {
                background-color: #2f80d1;
                color: white;
                padding: 10px 14px;
                font-size: 13px;
            }

            .topbar a {
                color: white;
                text-decoration: none;
                margin-right: 22px;
            }

            .title {
                font-weight: bold;
                margin-right: 18px;
            }

            .date-text {
                margin-right: 22px;
            }

            .container {
                padding: 8px 14px 20px 14px;
            }

            .section-tab {
                display: inline-block;
                padding: 8px 12px;
                border: 1px solid #d8d8d8;
                border-bottom: none;
                background-color: white;
                font-size: 12px;
                margin-bottom: 10px;
            }

            .toolbar {
                margin-bottom: 8px;
                font-size: 12px;
            }

            .toolbar select,
            .toolbar input {
                padding: 4px;
                border: 1px solid #d1d1d1;
            }

            .toolbar .right {
                float: right;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                font-size: 12px;
            }

            th, td {
                border-top: 1px solid #e1e1e1;
                border-bottom: 1px solid #e1e1e1;
                padding: 8px 10px;
                text-align: left;
                vertical-align: top;
            }

            th {
                background-color: #fafafa;
                font-weight: bold;
            }

            .filter-row td {
                background-color: white;
                padding: 6px 8px;
            }

            .filter-row input,
            .filter-row select {
                width: 95%;
                box-sizing: border-box;
                padding: 6px;
                border: 1px solid #d6d6d6;
                background-color: white;
            }

            .bottom-controls {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-top: 8px;
                font-size: 12px;
                color: #444;
            }

            .pagination span {
                display: inline-block;
                padding: 6px 10px;
                border: 1px solid #d0d0d0;
                margin-left: 4px;
                background: white;
            }

            .pagination .active {
                background: #f0f0f0;
            }
        </style>
    </head>
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
            Show
            <select>
                <option>3</option>
            </select>
            entries

            <span class="right">
                <form method="GET" style="display:inline;">
                    Filter <input type="text" name="search" value="">
                </form>
            </span>
        </div>

        <table>
            <tr>
                <th>Name</th>
                <th>Rank</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Office</th>
                <th>Research Interests</th>
                <th>Remarks</th>
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
    """

    for f in faculty_list[:3]:
        html += f.to_html()

    html += f"""
        </table>

        <div class="bottom-controls">
            <div>Showing 1 to {shown_rows} of {len(faculty_list)} entries</div>
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
    return html


if __name__ == "__main__":
    print("Content-Type: text/html\n")
    print(generate_html())

