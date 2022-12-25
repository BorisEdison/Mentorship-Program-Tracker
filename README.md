<h2 align="center">
  MPT<br/>
  <a href="https://diffuser.borisedison.in/" target="_blank">mpt.borisedison.in</a>
</h2>
<h4 align="center">A website for tracking all the progress in the student-teacher mentoring program</h4>
<div align="center">
  <img alt="Demo" src="MPT/MPT/static/content/mpt.png" />
</div>

## Built With

![Django](https://img.shields.io/badge/Django-0C4B33?&style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E75028?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-2A93C9?&style=for-the-badge&logo=css3&logoColor=white)
![Javascript](https://img.shields.io/badge/javascript-F7E018?&style=for-the-badge&logo=javascript&logoColor=white)
![jQuery](https://img.shields.io/badge/jquery-5897BD?&style=for-the-badge&logo=jquery&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-B51010?&style=for-the-badge&logo=jinja&logoColor=white)
![Bootsrap](https://img.shields.io/badge/Bootstrap-7952B3?&style=for-the-badge&logo=bootstrap&logoColor=white)
![DataTables](https://img.shields.io/badge/datatables-448BD7?&style=for-the-badge&logo=datatables&logoColor=white)
![ChartJS](https://img.shields.io/badge/Chartjs-F67174?&style=for-the-badge&logo=chart.js&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-0B7DCB?&style=for-the-badge&logo=sqlite&logoColor=white)
![iconify](https://img.shields.io/badge/iconify-1767AA?&style=for-the-badge&logo=iconify&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## What is MPT?  <a id="what"></a>
Mentorship Program Tracker aims to make tracking the progress of the mentees easier and digital for all educational institutions. We started by making the [design](https://www.figma.com/file/haofGDovUBBTcLC6TTpRqT/mentoring-project-tracking-app?node-id=65%3A91) using an online designing tool called Figma while the frontend of the project is made using HTML, CSS, Bootstrap, and Javascript. All of these combined are used to make a basic functional and responsive website. The website features a sign in and sign up page, the faculty , admin and student dashboards, student profiles, meeting scheduling, details regarding meetings and activity logs. We Later made the Database [Schema](https://drawsql.app/teams/student-599/diagrams/mpt-db-schema) using the tool drawSQL The backend is made using Django, an open-source python web framework used for rapid development, pragmatic, maintainable, clean design, and secure websites. It provides an inbuilt admin page with logs and user lists for ease of access to the user with admin role. Roles can be assigned by the admin to give different views to the users

### Roles
- Admin

    - Give staff status i.e. Faculty/Mentor status
    - View and edit info of all the registered users
    - Assign students to their respective mentors
    - Send announcements to selected users
    - View all scheduled or previous meetings


- Faculty
    - View all the assigned mentees on the dashboard
    - View and edit personal & academic mentee details
    - Send announcements to selected mentees
    - Schedule meeting with selected mentees

- Student
    - View and edit personal & academic details
    - View the announcements send by the mentor
    - Get update of the meetings scheduled by the mentor

## Contribute  <a id="contribute"></a>
Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

### Not sure where to start?  <a id="wheretostart"></a>

##### Step 1:

Download or clone this repository by using the command given below:

`
git clone https://github.com/BorisEdison/MPT.git
`

##### Step 2:

Install Virtual Environment:

- Windows <br>
`pip install --user virtualenv`

- Mac <br>
`sudo pip3 install virtualenv`

##### Step 3:
Setup Virtual Environment:

- Windows <br>
`python -m virtualenv env`

- Mac <br>
`virtualenv -p python env`

##### Step 4:
Activate Virtual Environment:

- Windows <br>
`env\scripts\activate`

- Mac <br>
`source env/bin/activate`

##### Step 5:

Install Requirements Packages:

`pip install -r requirements.txt`

##### Step 6:

Run Django Server:

`python manage.py runserver`

### Deployment  <a id="deployement"></a>
How To Deploy Django App with Nginx, Gunicorn, PostgreSQL and Let’s Encrypt SSL on Ubuntu - [Link](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

### Show your support

Give a ⭐ if you like this project and feel free to make pull requests

## License  <a id="license"></a>

Code release under the 
[MIT](https://github.com/BorisEdison/MPT/blob/main/LICENSE.txt) license
