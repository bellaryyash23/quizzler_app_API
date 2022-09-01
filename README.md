# Upgraded Quizzler App with GUI📱 using Tkinter, Requests API of Python

🌟Upgraded the earlier created quiz app to include a dynamic API request call for each run and created a GUI for the app, to enhance the user experience.

👉In the 'data.py' file which earlier contained static list of questions Now, is a dynamic question data created as it makes API request to GET question data for 
each app run. This data is passes to the 'main.py' file using module call.

👉The data imported from the 'data.py' file is formated in the 'main.py' file and a list of question & answer is created which, is passed to the 'quiz_brain.py' module.

👉Now the UI setup is done in the 'ui.py' file using the tkinter classes like Label, Button, Tk, Entry, PhotoImage and Canvas. The Canvas class is 
used to design the background image of the app.

👉The objects are placed and packed on the window using the .grid(..) method of the tkinter class which divides the whole window into rows and columns.

![UI design of App](https://github.com/bellaryyash23/quizzler_app_API/blob/master/samples/ui.JPG?raw=true)

👆UI Design of the App👆

👉In the 'ui.py' file, the QuizBrain class object is passed as a parameter. From the QuizBrain class the various methods to create next question are used to 
configure the question text in UI of the App.

![Question display of App](https://github.com/bellaryyash23/quizzler_app_API/blob/master/samples/question.JPG?raw=true)

👆Question display of the App👆

👉The quizz_brain.py is truely the brain of the Quiz. It performs the task of Updating questions, Keeping track of user score and track of
questions asked. All this is implemented by the use of QuizBrain class and its correspoding methods.

👉When user presses the correct option the Feedback is given in the form of background color change and score updation.

![Correct Answer](https://github.com/bellaryyash23/quizzler_app_API/blob/master/samples/right.JPG?raw=true)

👆App window for Right Answer👆

👉Alternatively when the user selects the wrong option the screen flashes red color and in this way the user gets a feedback for wrong answer.

![Wrong Answer](https://github.com/bellaryyash23/quizzler_app_API/blob/master/samples/wrong.JPG?raw=true)

👆App window for Wrong Answer👆

👉In the end, after user has attempted all the questions, a message is displayed on the app screen indicating the end of the quiz. The user can record their score and
in this way the GUI based Quiz App is implemented.

![End screen](https://github.com/bellaryyash23/quizzler_app_API/blob/master/samples/end.JPG?raw=true)

👆End Screen after Quiz end👆
