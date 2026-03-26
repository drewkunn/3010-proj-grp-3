#!/usr/bin/env python3
import psycopg2
class Faculty:
    def __init__(self, id, name, department, email):
       self.id = id
       self.name = name
       self.department= department
       self.email= email
    def to_html(self):
        return f"<tr><td>{self.name}</td><td>{self.department}</td><td>{self.email}</td></tr>"


def get_faculty_data(search=None):
    conn = psycopg2.connect(
        dbname="dashboard",
        user="webuser1",
        password="password",
        host="localhost",)
    cur = conn.cursor()
    if search:
        cur.execute(
            "SELECT * FROM faculty WHERE name ILIKE %s ORDER BY name;",
            ( '%' + search + '%',))
    else:
        cur.execute("SELECT * FROM faculty ORDER BY name;")
    rows = cur.fetchall()
    faculty_list = []
    for row in rows:
         f = Faculty(row[0],row[1],row[2],row[3])
         faculty_list.append(f)


    cur.close()
    conn.close()
    return faculty_list
def generate_html():
    import cgi
    form = cgi.FieldStorage()
    search = form.getvalue("search")

    faculty_list = get_faculty_data(search)
    html = ""

    html += """ 
    <div style="background-color:#592A8A; padding:15px;">
    <h1 style="color:white;">ECU CS Dashboard</h1>
    <a href="faculty.py" style="color:white; margin-right:15px;">Faculty</a>
    <a href="courses.py" style=color:white; margin-right:15px;">Courses</a>
    <a href="#" style="color:white; margin-right:15px;">SCH Drilldown</a>
    <a href="#" style="color:white; margin-right:15px;">FTE</a>
    <a href="#" style="color:white; margin-right:15px;">Faculty Committees</a>
    <a href="#" style="color:white;"> Resources</a>
    </div>
    """

    html += """
    <form method="GET">
        <input type="text" name="search" placeholder="Search name">
        <input type="submit" value="Search"> 
    </form>
    """
    html += "<table border='1'>"
    html += "<tr><th>Name</th><th>Department</th><th>Email</th></tr>"
    for f in faculty_list: 
        html += f.to_html()
    html += "</table>"
    return html
if __name__ == "__main__":
    print("Content-Type: text/html\n\n")
    print(generate_html())
