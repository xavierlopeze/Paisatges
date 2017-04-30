from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database_setup import Base, ClickCounter,Images, Matches

app = Flask(__name__)

engine = create_engine('sqlite:///paissatge.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

import random


@app.route('/', methods = ['GET','POST'])
@app.route('/competicio', methods = ['GET','POST'])
def HelloWorld():

    if request.method == 'POST':
        print request.form['submit1']

    	submit1 = request.form['submit1'].split()
        winnerImage = session.query(Images).filter_by(name=submit1[0]).one()
        loserImage  = session.query(Images).filter_by(name=submit1[1]).one()

    	winnerImage.wins = winnerImage.wins + 1
    	loserImage.loses = loserImage.loses + 1
    	
    	winnerImage.matches = winnerImage.matches + 1
    	loserImage.matches = loserImage.matches + 1

    	newMatch = Matches(winner = winnerImage.name, loser = loserImage.name, position = 1)
    	session.add(newMatch)
    	session.commit()

    	newClick = ClickCounter(name = 'someClick')
        session.add(newClick)
        session.commit()
        print session.query(ClickCounter).count()

        return redirect(url_for('HelloWorld'))

    else:
        rand1 = random.randrange(0, session.query(Images).count())
        rand2 = random.randrange(0,session.query(Images).count())
        while(rand1==rand2):
            rand2 = random.randrange(0,session.query(Images).count())
        image1 = session.query(Images)[rand1]
        image2 = session.query(Images)[rand2]    

    items = session.query(Images).all()
    matches = session.query(Matches).all()
    lastMatch = session.query(Matches).order_by(Matches.id.desc()).first()
    return render_template('participa.html',image1 = image1, image2=image2,items=items, matches = matches, lastMatch = lastMatch)

@app.route('/galeria', methods = ['GET','POST'])
def galeria():
    all_images = session.query(Images).all()
    return render_template('galeria.html', all_images = all_images)

@app.route('/mesvotats', methods = ['GET','POST'])
def mesVotats():
    all_images = session.query(Images).order_by(Images.wins)
    return render_template('galeria.html', all_images = all_images)

@app.route('/menysvotats', methods = ['GET','POST'])
def menysVotats():
    all_images = session.query(Images).order_by(Images.wins.desc())
    return render_template('galeria.html', all_images = all_images)

@app.route('/contacte', methods = ['GET','POST'])
def contacte():
    return render_template('contacte.html')



if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
 