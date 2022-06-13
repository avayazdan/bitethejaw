## Bite The Jaw (BTJ) - Solo Project

Deployed at: 

![btjlogo2](https://user-images.githubusercontent.com/75817925/168427314-5c471431-0d7d-404d-93dd-c6ef1d60bdcb.png)


## Project Requirements

This project was built for project four of General Assembly's Full-Stack Software Engineering course. The project aim was to build a website/application with our own API, utilise our growing knowledge of React and new-found knowledge of Python and Django. The project specs allowed us to take inspiration from complex websites/apps that use data such as AirBnb or Facebook, and essentially rebuild it in our own way if we desire, however, I decided to make a project about things I am passionate about and take inspiration from my own interests. The timeframe for this project was two weeks. 

### Table of contents 

1. Project aims & inspiration 
2. Planning 
3. Build
4. Styling
5. Challenges and Wins
6. Future improvements

### Project aim 

BTJ is a fictional political space where people can express themselves on current affairs, history, philosophy and more. The articles are sorted by categories: Art, Film Studies, Philosophy, History, Politics and Current Affairs. (stretch goal). The articles are accessed and available to view by anyone, however only registered users can submit a submission. 

The functionality of BTJ includes:

- Retrieve articles from the backend and display them to the user
- Register a user
- Login a user
- Submit an article when you are logged in

![image](https://user-images.githubusercontent.com/75817925/169652565-53f93d63-5369-4a1d-89f7-8b1119ced927.png)
![image](https://user-images.githubusercontent.com/75817925/169652576-a36d2e73-20e7-417b-b415-9cd14d90deec.png)
![image](https://user-images.githubusercontent.com/75817925/169652595-ffad7e89-cd44-4424-ad07-0b5815de435c.png)


### Planning 

![BTJ](https://user-images.githubusercontent.com/75817925/168427372-d741fbea-2520-439f-a41b-7db6279dad83.png)

Before the project: My planning started with creating a wireframe using Excalidraw, and speaking with my tutors on ideas that would be doable and sufficient for the project requirements.

During the project: I used Google Docs to keep a daily list of tasks I wanted to/needed to complete day by day, this helped me stay organised and know what to focus on as my next steps, whether that was asking a question from my tutors or implementing a function or styling etc. See example below:

![bjt screenshot readme](https://user-images.githubusercontent.com/75817925/168427352-1d77c206-4185-45de-bc05-0b11f03dafe1.png)

### Build

Frontend: The project utilises React, HTML and CSS.

How does it work? The frontend fetches data from the local API that I built in the backend and displays the information on the page, thus the articles are dynamic and not hardcoded, users can also register and login which will send data to the API. I used the typical React way of working, using components etc. 

In the below snippet, see the methodology used for fetching the data from my API and displaying it onto the page when the corresponding page with the particular ID is clicked via the homepage. Axios is fetching the particular submission from the submissions ID. Then we are basically saying if submissions is true, then return the category, image, text and so on (accessed by doing “submissions.image”) and if submissions is not true, return “loading…”. Which is what will show subsequently, when the submissions have not been fetched yet. Thus creating a clever loading effect. 

 ```

  const [submission, setSubmission] = React.useState(null)
  const { submissionsId } = useParams();

  React.useEffect(() => {
    console.log("hello ", submissionsId);


    axios({
      method: 'get',
      url: `http://localhost:8000/submissions/${submissionsId}`,
      // headers: {
      //   Authorization: `Bearer ${localStorage.getItem("token")}`,
      // },
    })
    .then((response) => {
      console.log(`submissions data: `)
      console.log(response.data);

        setSubmission(response.data);
        console.log("fetching data...")
    })
    .catch((error) => {
      console.log(error);
    })
  }, [submissionsId]);
  console.log()
  return (
    <>
      {submission ? 
        <div className="articles">
        <h2>{submission.title}</h2>
        <h2 className="article-h2">Category: {submission.category}</h2>
        <div className="article-container">
        <h3 className="article-text">{submission.text_field}</h3>
        <img className="article-image" alt="article-photograph" src={submission.image}></img>
        </div>
        <h1>About the author:</h1>
        {/* <h2>Submitted by: {submission.submitted_by}</h2> */}
          {/* <Link to={`/user/`}> 
        </Link>  */}
      </div> : <p>Loading...</p>}

 ```



Backend: The backend of this project utilises Python, Django and Poetry package manager. I also used Insomnia to test my routes and understand my models/data. I utilised the use of Django Generics and the Django user model, however I adjusted the user model to fit the needs of my project. Below is a snippet of how my models were set up. First, we have a list of tuples set to the variable “categories”, which we will then use in the choice field inside the model in order for the user to pick choices in a dropdown list. I found this a very cool feature of Django models. Most of the fields in the model are CharFields, as they correspond to the user entering text input, which was sufficient for this project. We can also see that the submitted_by field is using a foreign key with the user model and is thus corresponding with the user ID. 

 ```

CATEGORIES = [
    ('art', "Art"),
    ('history', "History"),
    ('philosophy', "Philosophy"),
    ('politics', "Politics"),
    ('poetry', "Poetry"),
    ('film_studies', "Film studies")
]


class Submissions(models.Model):
    """
    User submissons
    """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # submission_id = models.PositiveIntegerField(primary_key=True)
    # uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=200, default=None, null=True)
    image = models.CharField(max_length=200, default=None)
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    # submitted_by = models.ForeignKey(
    #     User, related_name="submitted_by", on_delete=models.PROTECT)
    date_submitted = models.DateField(auto_now_add=True)
    text_field = models.CharField(max_length=6000, default=None)
    category = models.TextField(
        choices=CATEGORIES,
        default=None,
    )

 ```



![helloooo](https://user-images.githubusercontent.com/75817925/168429865-92544cd9-edf7-41eb-b784-6e06ebd6b554.png)


### Styling

I wanted the styling of this project to represent the visual things I am passionate about: 15th-19th century art and photography, Christian imagery, plague doctors and so on. But I wanted the website to represent a modern feel, and not have an old-school vibe, but a more relevant one. I wanted to merge the historical things I am passionate about with modern website styling. I didn't use any styling frameworks for this project as I enjoy doing my own styling, however for future, I would like to learn how to use some CSS libraries or frameworks. Below, you can find my sketch of how I envisioned the layout of my homepage. 

![btj design outline](https://user-images.githubusercontent.com/75817925/168427385-bea1c2e3-ef06-4c72-9eb5-464be4e4de9f.png)

### Challenges & wins

#### Wins

A big win for me was working on my own and pushing myself to be patient with myself and my abilities when it comes to front-end engineering. It was my first time figuring things out on my own and I found that it was the first time I had pushed myself to overcome some of my imposter syndrome and work independently. 
Another win was realising how much I have a passion for design/styling and seeing my vision come to life, throughout my SEI course I have felt connected to styling and this final project really helped me see how much my skills have grown and how my passion for design has flourished and has inspired me to maybe take my design skills further.

#### Challenges 

The biggest technical challenge of this project was connecting the Username with the Submitted_by fields in my two models. It was possible to get the User ID however fetching the username was a challenge and I ended up not being able to implement this feature although I spent a lot of time researching and speaking to tutors about it. Another challenge was not knowing/having a gauge of how I was doing in the 2 weeks, and having to deal with the anxiety of the unknown and not having peers to discuss it with to ease the anxiety, however, in the end, this turned out to be okay as I was happy with where I was with my project and how far I got.


### Future improvements or changes

Features to implement: 

- Display author (logged in user who created the article) bio/picture/username
- Have a categories page, which will have links to the different categories, which will then show a list of articles with the relevant category (this was originally intended as a stretch goal)
- Add more data into the backend to display on the website
- Deployment
  

#### Key learnings / Main takeaways

I felt that I had a lot of personal growth throughout my time making this project. Working by myself on a full-stack application for the first time was enlightening in a myriad of ways. I had no one to comfort me if I was worried about time-restraints, no one to talk with about how I was getting along or if I was doing enough. I just had to trust my gut and keep going. I definitely had these sorts of worries during the project time. However, come project day, it was clear in the end that I had managed my time well, and that I really had a lot done within the given timeframe. Working independently on a project I was so passionate about for two weeks really helped me understand what sort of programmer I am, and helped me shed some of the imposter syndrome I was feeling for a long time prior to this project. I believe this project has contributed to my personal growth as a developer immensely, and has shown me how passionate I am about working in this field. 


