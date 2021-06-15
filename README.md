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

# How It's Made
## Theme Section (5pt)
- [Quote Page](https://p3cowboys.nighthawkcodingsociety.com/quote/) (+0.5pt User interaction, +0.5pt Technical, +1pt Fun)
    - Quote page demonstrates usage and display of [online APIs](https://github.com/TMarwah/P3Cowboys/blob/e641f16f5d17751b83b95b243ae1013c0167d6c7/main.py#L31)
    - User can refresh the page to get a new response each time
    - Quotes add to the theme of the project by giving users inspirational quotes to help with their buisness ideas
- [Upload Page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/upload.html) (+0.5pt User interaction, +0.5pt Technical, +1pt Fun)
    - Upload page demonstrates usage and display of user interaction 
    - User can upload their websites advertisement and then it will be viewable from the "Browse" page
    - This relates to the theme as it is the main point of interaction for the advertisements to be posted
- Database (+0.5pt User interaction, +0.5pt Technical)
    - This code shows the database that takes the user input from the upload page and connects it to the browse page.
    - [Link to full code for app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/app.py)
    - [Link to database setup part 1](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/model.py)
    - [Link to database setup part 2](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/db.py)
    - [Link for browse page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/browse.html)
## Individual Section (4.5pt)
- Blueprints (+4pt 4 labs)
    - [Each folder](https://github.com/TMarwah/P3Cowboys/tree/e641f16f5d17751b83b95b243ae1013c0167d6c7/Cowboys) is labled with the corresponding member to indicate their individual blueprint
- Technicals (+1pt 2 Technicals)
    - Each minilab utilizes [classes](https://github.com/TMarwah/P3Cowboys/blob/c44d5b580d1db0821e71453ef1be321120e6a9fd/Cowboys/Allen/minilab1.py#L2-L32) in order to pass in [parameters](https://github.com/TMarwah/P3Cowboys/blob/c44d5b580d1db0821e71453ef1be321120e6a9fd/Cowboys/Allen/app.py#L130) that cause different functions to run 
    - 
## API Section (3pt)
- [API and Receiving](https://p3cowboys.nighthawkcodingsociety.com/quote/) (+2 Receive and API, +1 Visual)
    - API for quotes is used [here](https://github.com/TMarwah/P3Cowboys/blob/e641f16f5d17751b83b95b243ae1013c0167d6c7/main.py#L31) and the author and quote is stored as jinja variables
    - Jinja variables are then displayed on the front end [here](https://github.com/TMarwah/P3Cowboys/blob/d829f25775a369d12d43b9ad72c38f556e9b9064/templates/quotepage.html#L140-L150)
    - Used png of quotes to emphasize the quote and highlighted text to be easily seen, with author cited at bottom right as well
## Deployment Section (5pt)
- How It's Made section (+2pt How Its Made, +1pt Visuals)
    - Located in readme, section is labled How Its Made, is what you are currently looking at
- Commercial (+2pt)
    - [Link to video](https://www.youtube.com/watch?v=XnYaSJoKWxE&ab_channel=Purplebears)
# Code Explanations
## Profile Page (Karam)
- [Link to the app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Karam/app.py)
- [Link to full code for profile page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Karam/templates/Dashboard.html) 
```
from flask import Blueprint, render_template, request

from .karamminilab import Caracal, Characters, bubblesort

Cowboys_Karam_bp = Blueprint('Cowboys_Karam', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')
@Cowboys_Karam_bp.route("/")
def upload():
    return render_template ("homepage2.html")

@Cowboys_Karam_bp.route("/karamminilab")
def minilab():
    caracals= [Caracal("skinny", "beige"), Caracal("fat", "brown")]
    return render_template("karamminilab.html", caracals=caracals)


@Cowboys_Karam_bp.route("/karambubblesort.html", methods=["POST", "GET"])
def qaracters():
    if request.method == 'POST':
        string = request.form.get('word')
        word = str(string)
        return render_template("karambubblesort.html", characters=Characters(word).characters)
    return render_template("karambubblesort.html")


@Cowboys_Karam_bp.route("/otherubblesort", methods=["POST", "GET"])
def minilabs():
    if request.method == 'POST':
        bubble = request.form.get('character')
        return render_template("otherubblesort.html", output = bubblesort(bubble).bubblesort)

    return render_template("otherubblesort.html")


@Cowboys_Karam_bp.route("/Dashboard")
def model():
    return render_template("/Dashboard.html", model=model)

```
## Login Page (Tanmay)
- This code shows the login page that accepts a username and password then identifies the user
- [Link to full code for app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Tanmay/app.py)
- [Link for login page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Tanmay/templates/login.html)
```
from flask import Blueprint
from flask import render_template, request
from Cowboys.Tanmay.tanmayminilab import  Counters

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@Cowboys_Tanmay_bp.route('/login', methods=["POST", "GET"])
def login_route():
    logform = LoginForm()
    if logform.validate_on_submit():
        user = User.query.filter_by(username=logform.username.data).first()
        if user is None or not user.check_password(logform.password.data):
            flash("Login Failed")
            return redirect("/login")
        login_user(user)
        flash("Login Successful!")
        if logform.username.data == "secret":
            return redirect("/secret")
        nextpage = request.args.get("next")
        if not nextpage or url_parse(nextpage).netloc != '':
            return redirect('/')
        return redirect(nextpage)
    else:
        return render_template("login.html", form = logform)

@Cowboys_Tanmay_bp.route('/minilab', methods=["POST", "GET"])
def minilab():
    if(request.method == 'POST'):
        sentence = request.form.get('sentence')
        sentencesort = request.form.get('sentencesort')
        input = sentence
        input2 = sentencesort
        return render_template("tanmayminilab.html",wordcount = Counters(input).wordcount(),
                               lettercount = Counters(input).lettercount(), sorted = Counters(input2).bubblesort())

    return render_template("tanmayminilab.html",wordcount = Counters(2).wordcount(),
                           lettercount = Counters(2).lettercount(), sorted = Counters(2).bubblesort())
```
## Database (Marc)
- This code shows the database that takes the user input from the upload page and connects it to the browse page.
- [Link to full code for app.py](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/app.py)
- [Link to database setup part 1](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/model.py)
- [Link to database setup part 2](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/db.py)
- [Link for browse page](https://github.com/TMarwah/P3Cowboys/blob/main/Cowboys/Allen/templates/browse.html)
```
@Cowboys_minilab1_bp.route('/cowboys/minilab1/browse')
def browse():
    backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/818606015494094868/812382.png"]
    review_query = Review.query.all()
    reviews = []

    for review in review_query:
        websiteurl = url_for('get_img', id=review.id)

        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'image':  websiteurl
        }
        reviews.append(review_dict)
    return render_template("browse.html", reviews=reviews, background=random.choice(backgrounds))
    
@Cowboys_minilab1_bp.route('/cowboys/minilab1/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["username"]
        content = request.form["content"]
        image = request.files.get('img')
        if not image:
            return 'bad news ur image did not make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, mimetype=mimetype)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("browse.html"))
    return render_template("upload.html", background=background)
    
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

# Pre Final Project Team Checkpoint
NAME             | Accomplishment |
-------------    | --------------- |
William Cherres  | I worked on the UI with Karam and was able to make the feedback page look more proffesional. I then was able to reconnect the Feedback Page back to the Response Page as it was disconnected when Karam and I re-did the whole Feedback Page. [Ticketin Progress](https://github.com/TMarwah/P3Cowboys/issues/41) [Ticket In review](https://github.com/TMarwah/P3Cowboys/issues/38) |
Allen Xu| Contineud work on the database and started to look into how to create our own API. We also have future plans to work with the P4 KPOP group and utlize their API onto our website. [Ticket in Progress (browse page)](https://github.com/TMarwah/P3Cowboys/issues/22) [Ticket in Review (API and database)](https://github.com/TMarwah/P3Cowboys/issues/40) | 
Marc Humeau| I worked on the browse page and was able to create a page that will be used for displaying business posts from the upload page in the future. I worked on this with Allen as he worked on the upload page with the form submission. [Ticket in Progress](https://github.com/TMarwah/P3Cowboys/issues/39), [Ticket in Review](https://github.com/TMarwah/P3Cowboys/issues/15) |
Tanmay Marwah  | I finished the login UI and have started to work on establishing the database for the username and password storage [Ticket in Progress (database)](https://github.com/TMarwah/P3Cowboys/issues/9) [Ticket in Review (UI and Login fields)](https://github.com/TMarwah/P3Cowboys/issues/1) |
Karam Alshaikh |I worked on the UI with Billy and mainly focused on improving the functionality of the feedback and login/sign up page, creating a more professional look for the website [Ticketin Progress](https://github.com/TMarwah/P3Cowboys/issues/28) and [Ticket In review](https://github.com/TMarwah/P3Cowboys/issues/27) |   |

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
