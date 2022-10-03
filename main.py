# main.py

from flask import Flask, render_template, request
import cohere
co = cohere.Client("TkPa2y63AqaCNl6v1gfN7LTloymxVMwJGH0FMIbE")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  ## finds the index.html file under the templates folder


@app.route('/generate', methods=['GET'])  ## an existing "action" should be created
# for this endpoint
def generate():
    prompt = """
This program will generate a short story given the title of the story.
--
Starter: Once upon a time
Genre: Fairy Tale, Fantasy
Story: Once upon a time, in a city far far away, there lived a beautiful princess named Fiona.
But she was cursed from a very young age, a curse where she would transform into a 
hideous ugly ogre. Beautiful princess by day, ugly ogre by night. In order to hide this curse of
hers, Fiona got locked up in the smallest room of the tallest tower guarded by a dangerous dragon.
Only true love's kiss can overturn the curse, but no one dares to save the princess.
--
Starter: In the deserted land of Egypt n 1977
Genre: Science-fiction, thriller
Story: In the deserted land of Egypt in 1977, there lived a cheerful little boy called Abdul who was loved by all who met him. Except 
for his jealous older brothers who envied the young boy. The brothers devised a plan to get rid of her. They
carefully brought their younger brother in the middle of the forest and tricked him to fall into a well. The 
brothers then left Abdul and ran away. The brothers convinced their father that the youngest had run away, 
and so they named him the Runaway.
--
Starter: There once lived a pirate named Jack 
Genre: Adventure
Story: There once lived a pirate named Jack a long time ago. He was feared by most due to his unfortunate
looks, but he had a heart of gold. He was on the lookout for the greatest treasure of them all, the one
that everyone sought, a literal heart made of gold. It was said to be a miracle that fell from the sky. And
so, he set off to sail across the oceans, in search of the treasure.
--
Starter: A guy liked to go on dance floors
Genre: thriller, detective 
Story: A guy liked to go on dance floors, when during one night, he witnessed the worst scene he ever saw 
with his own eyes. Murder, murder on the dance floor. The reason, you may ask ? Well the victim refused to dance
for the bar owner and so the owner shot him down courtesy of the Disco Killer Club.
--
Starter:"""

    userPrompt = request.args.get('promptInput')
    genre = request.args.get('genreInput')

    print(userPrompt)
    print(genre)

    current_prompt = " " + userPrompt + "\nGenre: " + genre + "\nStory: "
    def generate_text(base_prompt, current_prompt):
        response = co.generate(
            model='xlarge',
            prompt=base_prompt + current_prompt,
            max_tokens=500,
            temperature=5,
            stop_sequences=["--"])
        generation = response.generations[0].text

        return generation

    return render_template("index.html", text=generate_text(prompt, current_prompt))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
