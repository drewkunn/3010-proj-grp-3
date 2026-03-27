#!/usr/bin/env python3
import psycopg2


class Course:
    def __init__(self, course_id, number, title, gu, ch, frequency, active, notes):
        self.course_id = course_id
        self.number = number
        self.title = title
        self.gu = gu
        self.ch = ch
        self.frequency = frequency
        self.active = active
        self.notes = notes

    def to_html(self):
        active_text = "Yes" if self.active else "No"
        return f"""
        <tr>
            <td>{self.number}</td>
            <td>{self.title}</td>
            <td>{self.gu}</td>
            <td>{self.ch}</td>
            <td>{self.frequency}</td>
            <td>{active_text}</td>
            <td>{self.notes}</td>
        </tr>
        """


def get_course_data():
    conn = psycopg2.connect(
        dbname="dashboard",
        user="webuser1",
        password="password",
        host="localhost"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM courses ORDER BY number;")
    rows = cur.fetchall()

    course_list = []
    for row in rows:
        c = Course(
            row[0],  # course_id
            row[1],  # number
            row[2],  # title
            row[3],  # gu
            row[4],  # ch
            row[5],  # frequency
            row[6],  # active
            row[7]   # notes
        )
        course_list.append(c)

    cur.close()
    conn.close()
    return course_list


def generate_html():
    course_list = get_course_data()

    html = """
    <html>
    <head>
        <title>ECU CS Dashboard - Courses</title>
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

            .subtabs {
                border-bottom: 1px solid #d8d8d8;
                margin-bottom: 10px;
                padding-top: 2px;
            }

            .subtabs a {
                display: inline-block;
                padding: 8px 12px;
                margin-right: 2px;
                border: 1px solid #d8d8d8;
                border-bottom: none;
                background-color: #f7f7f7;
                color: #333;
                text-decoration: none;
                font-size: 12px;
            }

            .subtabs a.active {
                background-color: white;
                font-weight: bold;
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

            .column-btn {
                margin-bottom: 8px;
            }

            .column-btn button {
                border: 1px solid #bcbcbc;
                background-color: #f2f2f2;
                padding: 6px 10px;
                font-size: 12px;
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

            .notes-col {
                width: 38%;
            }

            .small-col {
                width: 7%;
            }

            .medium-col {
                width: 10%;
            }

            .title-col {
                width: 22%;
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
        <div class="subtabs">
            <a href="#" class="active">Course Info</a>
            <a href="#">Course Directors</a>
            <a href="#">Course Schedule History</a>
            <a href="#">SCH Generated</a>
        </div>

        <div class="column-btn">
            <button>Column visibility</button>
        </div>

        <div class="toolbar">
            Show
            <select>
                <option>10</option>
            </select>
            entries

            <span class="right">
                Filter <input type="text">
            </span>
        </div>

        <table>
            <tr>
                <th class="medium-col">Number</th>
                <th class="title-col">Title</th>
                <th class="small-col">GU</th>
                <th class="small-col">CH</th>
                <th class="small-col">Frequency</th>
                <th class="small-col">Active</th>
                <th class="notes-col">Notes</th>
            </tr>

            <tr class="filter-row">
                <td><input type="text"></td>
                <td>
                    <select>
                        <option>All</option>
                    </select>
                </td>
                <td><input type="text"></td>
                <td><input type="text"></td>
                <td><input type="text" style="background-color:#e7e7e7;"></td>
                <td><input type="text"></td>
                <td>
                    <select>
                        <option>All</option>
                    </select>
                </td>
            </tr>
    """

    for c in course_list:
        html += c.to_html()

    html += """
        </table>
    </div>

    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    print("Content-Type: text/html\n")
    print(generate_html())
