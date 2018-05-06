# Alexa-Calculus
Nicholas Vitebsky, Abhi Sarma, Brian Lee

__Won Best IoT Hack at HackMCST III__

# Inspiration
We came up with the project on a whim. We had initially toyed with an API for both NJ Transit and NYC Transit, apps for testing the performances of various CS algorithms. We had an Amazon Alexa for some weird purpose. Three hours later and we had no project idea. Then Brian the Github man remembered the two 70s he got on his calc tests. He thought, why not have Alexa do his calc homework? Nah, there's an app for that, he said. Except there wasn't. Thus our app.

# What it Does

Alexa Calculus takes a function inputted by voice and computes the derivative (or the integral) of the function. The only other calculus app in the Alexa marketplace only knew the derivative of sin x (or trigonometric apps if you were lucky), so we considered it inadequate.

NOTE: running this app requires either a) Beta Access given from one of the developers or b) re-compiling the project by making a new Skill. The project is in lieu of being approved by Amazon.

# How we Built it

The project utilizes a Python core and takes data from a Wolfram Alpha API. There are two sides to the project:
1. **Wolfram-Side**: Takes the user-input command and inputs into the API to get a result (hopefully another function) to release back to the user.
2. **Alexa-Side**: a) processes the words the user says and b) recieves the output and sends it to Alexa to speak. 

The Wolfram-Side relies on a classic Get/Post REST API, and the Alexa-Side relies on a series of preset "commands" to quickly process the command and send it along its way.

# Challenges we Ran Into

Immense challenges emerged over the Alexa-Side of the project. This was partially because the documentation was inadequate, and partially because our experience with Alexa was limited. Perhaps the most tough experience was processing and extracting the voice command to send to the Wolfram-Side, in particular because little documentation existed on how to link Alexa's script with our core Python files.

The final major issue was how Alexa recieved the results. The initial strategy was to encompass a JSON file with ```json.loads()``` (to make a JSON file), but that turned out to be unecessary.

# Accomplishments We're Proud Of

This project is a major implementation of Git branching and proved substantial training on generating efficient and robust workflows, adapting to which is an essential to getting CS jobs. This project made clear the dangers of bad documentation, but also highlights the advantages of good documentation. (e.g. regarding the Wolfram-Side)

# What We Learned

1. Beware of Alexa.
2. Good Documentation is a good thing.
3. Working with a team is almost always better than alone.

# What's Next

Implementation of ```git rebase``` is a suitable target if the project is continued. The application will reasonably be extended to other concepts in calculus (e.g. series)

# Built With
- Python
- Alexa 

Always remember zip man
