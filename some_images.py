from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Images
engine = create_engine('sqlite:///paissatge.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


images_names = [
	'montserrat.jpg',
	'girona.jpg',
	'lamolina01.jpg',
	'montserrat11.jpg',
	'montserrat04.jpg',
	'parc_tibidabo11.jpg',
	'parc_tibidabo09.jpg',
	'girona04.jpg'
	]

inputs = []
for name in images_names:
	inputs.append(Images(name = name, 
			description = 'No description avaliable yet.',
			matches = 0, wins = 0, loses = 0))
for input in inputs:
	session.add(input)
session.commit()

