## Important Note
# We should have erverthing working if you (revert the current snapshot) everthing should autumaticly pop up and show. We have everything in the web vm exept the fte calculations dont show in the (webvm) but they do show on our (main vm) if you want to verify.





# Project Setup Instructions

## 1. Start the VM

## 2. Open Terminal

## 3. Stop Local PostgreSQL
(so Docker can use port 5432)
```bash
sudo systemctl stop postgresql
```

## 4. Start the Database Container
```bash
sudo docker start pg-db
```

If the container does not exist:
```bash
sudo docker run -d --name pg-db -p 5432:5432 phase4-db
```

## 5. Restart Apache
```bash
sudo systemctl restart apache2
```

## 6. Test Database Connection
```bash
PGPASSWORD=password psql -h localhost -p 5432 -U webuser1 -d dashboard -c "SELECT COUNT(*) FROM faculty;"
```

**Expected Output:**
```text
count
-------
7
```

## 7. Open Website in Browser
- http://localhost/cgi-bin/faculty.py  
- http://localhost/cgi-bin/courses.py  
- http://localhost/cgi-bin/fte.py  

---

## Notes
- Database runs inside a Docker container  
- User: `webuser1`  
- Password: `password`  
- Database name: `dashboard`  

---

## Troubleshooting

### Restart Container
```bash
sudo docker restart pg-db
```

### Restart Apache
```bash
sudo systemctl restart apache2
```

### Restore Database (if needed)
```bash
sudo docker exec -i pg-db psql -U postgres -d dashboard < backup_dashboard.sql
```

## Submission Details
* [cite_start]**Project Branch**: All files are maintained in the `phase4` branch of the GitHub repository[cite: 40].
* [cite_start]**Archive**: The full project directory has been compressed into `phase4_final.tar` for submission[cite: 45].
