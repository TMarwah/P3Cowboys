# P3 Cowboys Advertisement site
GitHub Repo for the Period 3 Cowboys Team
# Links
- [Website link](http://p3cowboys.pentahex.xyz:8080/)
- [Project Ticket Board](https://github.com/TMarwah/P3Cowboys/projects/1)
- [Project Plan + Ideas](https://docs.google.com/document/d/1NUglOHAQ0yPWXlH5ESuNnhjRK4Zx0Qv2SCLvOVtnDrY/edit?usp=sharing)
- [Blueprints for project with different url for each person](https://github.com/TMarwah/P3Cowboys/blob/2171223a6bce49fae78ed343d555b93a0db4597a/app/app.py#L16-L20)
# Creators & Github Links
NAME             | GITHUB Link |
-------------    | --------------- |
William Cherres  | https://github.com/BillyCherres  |
Allen Xu| https://github.com/allenyxu | 
Marc Humeau| https://github.com/marchumeau|
Tanmay Marwah  | https://github.com/TMarwah |
Karam Alshaikh |https://github.com/KaramAlshaikh |


# Project Code Snippets (Layout for final project presentation)
## Browse Page (Allen)
- This code shows blah blah blah
- Link to full code: 
```
Insert code snippet here
```
## Profile Page (Karam)
- This code shows blah blah blah
- Link to full code: 
```
Insert code snippet here
```
## Login Page (Tanmay)
- This code shows blah blah blah
- Link to full code: 
```
Insert code snippet here
```
## Database (Marc)
- This code shows blah blah blah
- Link to full code: 
```
Insert code snippet here
```
## Feedback Page (Billy)
- This code snippet shows the Usage of Get and Post to retrieve feedback and post it on the response page.
- [Link to full code of app.py](https://github.com/TMarwah/P3Cowboys/blob/19fdd8cef62f8a8a662cf7a78a3730db92d346da/Cowboys/William/app.py#L1-L75)(Connects feedback/response pages together using Get and Post)
- [link to full code of feedback page](https://github.com/TMarwah/P3Cowboys/blob/d97d3988f9a8f043502862bf08fa68c03e42bae4/Cowboys/William/templates/feedback.html#L1-L106)(Feedback page html shows user input)
- [link to full code of response page](https://github.com/TMarwah/P3Cowboys/blob/7805f62499a5afa35aff51be5356c4b1cb0f3f20/Cowboys/William/templates/response.html#L1-L152)(Response page html shows jinja funtions)
```
@Cowboys_William_bp.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('comment')
        input1 = name
        input2 = comment
        return render_template("response.html", name=name, comment=comment, input1=input1, input2=input2)
    return render_template("feedback.html")
```

# Final Umbrella Progress tickets
**This is the groups current progess/plans for the final project**
- This [video link](https://www.youtube.com/watch?v=SjYZ88i40iQ&ab_channel=Purplebears) shows the groups progress and plans for the final project described in the table below.

NAME             | Plans/Roles |
-------------    | --------------- |
William Cherres [Ticket in progress](https://github.com/TMarwah/P3Cowboys/issues/38) [Ticket in Review](https://github.com/TMarwah/P3Cowboys/issues/13)| Work on a Feedback and Response page. It is still being debated whether or not the feedback would be stored in a data base or not. But the Plan is to have a functional feedback and rerturn page that is connected through Get and Post.|
Allen Xu        .[Ticket in progress](https://github.com/TMarwah/P3Cowboys/issues/40) [Ticket in Review](https://github.com/TMarwah/P3Cowboys/issues/37)| Create table for storing the required elements the user uploads in the model.py file. This will be our database, which we can later add on to with thing such as the feedback page | 
Marc Humeau     .[Ticket in progress](https://github.com/TMarwah/P3Cowboys/issues/39) [Ticket in Review](https://github.com/TMarwah/P3Cowboys/issues/15)| Work on database that stores user inputted information about business, and then display it onto a browse page that is style similarly like Instagram. This will work in tandom with the user input field developed by Allen|
Tanmay Marwah  .[Ticket in progress](https://github.com/TMarwah/P3Cowboys/issues/9) [Ticket in Review](https://github.com/TMarwah/P3Cowboys/issues/1)| Create user login page that checks for credentials stored in the database, as well as locks the user out from accessing the rest of the site until they have authenticated.  |
Karam Alshaikh .[Ticket in progress](https://github.com/TMarwah/P3Cowboys/issues/28) [Ticket in Review](https://github.com/TMarwah/P3Cowboys/issues/27)| Work on deployment material; creating website domain and adding a user profile page where the user can post feedback and see their following, etc. | 

# Mini Lab

**Note:**
- Minilab commits for each person can be viewed in each individual directory [under Cowboys](https://github.com/TMarwah/P3Cowboys/tree/main/Cowboys)

NAME             | Goal |   Accomplished |
-------------    | --------------- | --------------- |
William Cherres |  Create blue print |[Blue Print](https://github.com/TMarwah/P3Cowboys/tree/main/Cowboys/William)|
Allen Xu|  Create blue print| [Blue Print](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/allenminilab.py)|
Marc Humeau|Create blue print |[Blue Print](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Marc/marcminilab.py)|
Tanmay Marwah  | Create blue print |[Blue Print](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Tanmay/tanmayminilab.py)|
Karam Alshaikh |Create blue print |[Blue Print](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Karam/karamminilab.py)|

# Crossover review
Individual Completed Tickets:
NAME             | Assingment | What was Finshed|
-------------    | --------------- | ------------- |
William Cherres |  [Home Page Ticket](https://github.com/TMarwah/P3Cowboys/projects/1#card-57480117) |I was able to create a home page. The idea was to make a simple easy page where the user can easily navigate through in order to get to the their desired destination. Here is the code for the [Home page Code](https://github.com/TMarwah/P3Cowboys/blob/5ec57777451284357de9c705b95008fdec0bacc1/app/templates/homepage.html#L1-L35)/[Blueprint](https://github.com/TMarwah/P3Cowboys/blob/6d19643be35fa7d889aedd4e8a080f27314306f8/Cowboys/William/app.py#L1-L10)|
Allen Xu| [Upload Page Ticket(Back End)](https://github.com/TMarwah/P3Cowboys/blob/5a36755e97b8ec6538fe84390580bed753aa9c89/Cowboys/Allen/templates/upload.html#L157-L185) |Front end for upload page can be seen [here](https://github.com/TMarwah/P3Cowboys/blob/c8e9c343fb768c091edd3bf91ee3eb6367120cc9/y2021/tri1/upload.html#L157-L190). Currently using template from Trish as a baseline for our upload form, though back end isn't fully functioning yet|
Marc Humeau| [Upload Page Ticket (Front End)](https://github.com/TMarwah/P3Cowboys/projects/1#card-57452895)|Created a base page that will be used to contain the [browse page](https://github.com/TMarwah/P3Cowboys/blob/1fe9f1baac450d288e187b750c9f2189ed094a49/Cowboys/Allen/templates/upload.html#L1-L185) in the future. Will work with the uploading database to pull data and display it in a Instagram like post.|
Tanmay Marwah  | [Sign up page Ticket](https://github.com/TMarwah/P3Cowboys/projects/1#card-57452127)|Created sign up and login page [Link](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Tanmay/templates/login.html). This allows the user to create an account from which they can upload advertisements. Registered users are the only people that can upload ads, but anyone can view them on the main page.|
Karam Alshaik | [deployment/ profile page Ticket](https://github.com/TMarwah/P3Cowboys/projects/1#card-57713701)|[Website link](http://p3cowboys.pentahex.xyz:8080/)|

# Project Plan:
[Link to full project plan](https://docs.google.com/document/d/1NUglOHAQ0yPWXlH5ESuNnhjRK4Zx0Qv2SCLvOVtnDrY/edit?usp=sharing)
## Project Idea
- **A website where you can upload advertisements for your business. (Instagram styled)**
- [ ] Ability to create accounts
- [ ] Once logged in, able to share advertisments with captions
- [ ] Explore tab has advertisements from all authorized users
- [ ] If not signed in, will see posts from official Cowboys account
- [ ] Able to explore other peoples work through the Browse page
- [x] Code is formatted through Blueprints
 


### College Board Requirements
- Instructions for input from one of the following:
  - the user (including user actions that trigger events)
  - a device
  - an online data stream
  - a file
- Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
- At least one procedure that contributes to the program’s intended purpose,
where you have defined:
  - the procedure’s name
  - the return type (if necessary)
  - one or more parameters
- An algorithm that includes sequencing, selection, and iteration that is in the
body of the selected procedure
- Calls to your student-developed procedure
- Instructions for output (tactile, audible, visual, or textual) based on input and
program functionality
