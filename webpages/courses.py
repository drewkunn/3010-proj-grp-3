#!/usr/bin/env python3
import cgi
import psycopg2
print("Content-Type: text/html\n\n")
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
        return (
            f"<tr> "
            f"<td>{self.number}</td>"
        f"<td>{self.title}</td>"
        f"<td>{self.gu}</td>"
        f"<td>{self.ch}</td>"
        f"<td>{self.frequency}</td>"
        f"<td>{'Yes' if self.active else 'No'}</td>"
        f"<td>{self.notes}</td>"
        f"</tr>"
    )
def get_course_data():
    conn = psycopg2.connect(
            dbname="dashboard",
        user="webuser1",
        password="password",
        host="localhost",
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses ORDER BY number;")
    rows = cur.fetchall()
    course_list = []
    for row in rows:
        c = Course(row[0], row[1], row [2], row[3], row[4], row[5], row[6], row[7])
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
               font-family: Arial,sans-serif;
               margin: 0;
               padding: 0;
           }
           .navbar {
               backround-color: #2d2dbb;
           color: white;
               padding: 20px;
               }
               .navbar h1 {
            margin: 0 0 15px 0;
           }
           .navbar a {
           color: white;
               text-decoration: underline;
               margin-right: 20px;
               font-size: 16px;
           }
           .content {
               padding: 15px;
           }
           table {
               border-collapse: collapse;
               width: 100%;
               max-width: 1200px;
           }
           th, td {
           border: 1px solid #999;
               padding: 8px;
           text-align: left;
               vertical-align: top;
           }
           th {
           backround-color: #f2f2f2;
           }
           h2 {
           margin-top: 0;
           }
       </style>
       </head>
       <body>
       <div class="navbar">
           <h1> ECU CS Dashboard</h1>
           <a href="/cgi-bin/faculty.py">Faculty</a>
           <a href="/cgi-bin/courses.py">Courses</a>
           <a href="#">SCH Drilldown</a>
           <a href="#">FTE</a>
           <a href="#">Faculty Commitees</a>
           <a href="#">Resources</a>
       </div>
       <div class="content">
           <h2>Course Information</h2>
           <table>
           <tr>
               <th>Number</th>
               <th>Title</th>
               <th>GU</th>
                   <th>CH</th>
               <th>Frequency</th>
                   <th>Active</th>
                   <th>Notes</th>
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
    print(generate_html())
