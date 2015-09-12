from flask import Flask, render_template, request, redirect
import jinja2
import os
# import quotes
QUOTES = ["I learned the game from William Wesley", "Back to back", "Back to back like I'm on the cover of Lethal Weapon", "Back to back like I'm Jordan '96, '97", "Whoa, very important and very pretentious", "When I look back I might be mad that I gave this attention", "Yeah, but it's weighin' heavy on my conscience", "You gon' make me step out of my fuckin' frame", "You gon' make me buy bottles for Charlamagne", "I drove here in the Wraith playin' AR-AB", "I'm not sure what it was that really made y'all mad", "But I guess this is what I gotta do to make y'all rap", "mad cause I got the midas touch", "Is that a world tour or your girl's tour?", "This ain't what she meant when she told you to open up more", "Yeah, trigger fingers turn to twitter fingers", "Make sure you hit him with the prenup", "I got the drink in me goin' back to back", "Please, check 'em for a wire or a earpiece", "Please, think before you come for the great one", "They gon' ask if I can play this shit back to back", "Runnin' through the 6 with my woes", "Countin' money you know how it goes", "Pray the real live forever man", "Pray the fakes get exposed", "I want that Ferrari then I swerve", "I want that Bugatti just to hurt", "I don't like how serious they take themselves", "I've always been me I guess I know myself", "My city too turnt up I'll take the fine for that", "Then Kanye dropped, it was polos and backpacks", "Man I'm talkin' way before hashtags", "I was runnin' through the 6 with my woes", "You know how that should go"]

app = Flask(__name__)

def word_count(x):
	s = x.split(" ")
	return len(s)

@app.route('/')
def hello():
	try:
		words = int(request.args.get("words"))
	except:
		return render_template("index.html")
	if words != "":
		matched = []
		for x in QUOTES:
			if word_count(x) == words:
				matched.append(x)
		# 	# matched.append(word_count(x))
		# 	matched.append(1)
		return render_template("quotes.html", quotes=matched)
	return render_template("index.html")

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)