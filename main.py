from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)

#Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#Creation of Song Table
class SongModel(db.Model):
	print(" I am in model class")
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	duration = db.Column(db.Integer, nullable=False)
	uploaded_time = db.Column(db.String(100), nullable=False)

#Creation of  Podcast Table
class PodcastModel(db.Model):
	print(" I am in model class")
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	duration = db.Column(db.Integer, nullable=False)
	uploaded_time = db.Column(db.String(100), nullable=False)
	host = db.Column(db.String(100), nullable=False)
	participants = db.Column(db.String(100), nullable=True)

#Creation of AudioBook Table  
class AudioBookModel(db.Model):
	print(" I am in model class")
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	author = db.Column(db.String(100), nullable=False)
	narrator = db.Column(db.String(100), nullable=False)
	duration = db.Column(db.Integer, nullable=False)
	uploaded_time = db.Column(db.String(100), nullable=False)

#def __repr__(self):
#	return f"Audio(name = {name}, duration = {duration}, uploaded_time = {uploaded_time})"

#create table
#db.create_all()
#Put values in Song table
song_put_args = reqparse.RequestParser()
song_put_args.add_argument("name", type=str, help="Name of the song is required", required=True)
song_put_args.add_argument("duration", type=int, help="Duration of the song is required", required=True)
song_put_args.add_argument("uploaded_time", type=str, help="Time of upload for Song is required", required=True)

#Put values in Podcast
pod_put_args = reqparse.RequestParser()
pod_put_args.add_argument("name", type=str, help="Name of the podcast is required", required=True)
pod_put_args.add_argument("duration", type=int, help="Duration of the podcast is required", required=True)
pod_put_args.add_argument("uploaded_time", type=str, help="Time of upload for podcast is required", required=True)
pod_put_args.add_argument("host", type=str, help="Host of the podcast is required", required=True)
pod_put_args.add_argument("participants", type=str, help="Participants of the podcast")

#Put values in AudioBook
book_put_args = reqparse.RequestParser()
book_put_args.add_argument("name", type=str, help="Name of the book is required", required=True)
book_put_args.add_argument("author", type=str, help="Author of the book is required", required=True)
book_put_args.add_argument("narrator", type=str, help="Name of the book is required", required=True)
book_put_args.add_argument("duration", type=int, help="Duration of the book is required", required=True)
book_put_args.add_argument("uploaded_time", type=str, help="Time of upload for book is required", required=True)

#Update values in song table
song_update_args = reqparse.RequestParser()
song_update_args.add_argument("name", type=str, help="Name of the song is required")
song_update_args.add_argument("duration", type=int, help="Duration of the song is required")
song_update_args.add_argument("uploaded_time", type=str, help="Time of upload for Song is required")

#Update values in podcast table
pod_update_args = reqparse.RequestParser()
pod_update_args.add_argument("name", type=str, help="Name of the podcast is required")
pod_update_args.add_argument("duration", type=int, help="Duration of the podcast is required")
pod_update_args.add_argument("uploaded_time", type=str, help="Time of upload for podcast is required")
pod_update_args.add_argument("host", type=str, help="Host of the podcast is required")
pod_update_args.add_argument("participants", type=str, help="Participants of the podcast")

#Update values in book table
book_update_args = reqparse.RequestParser()
book_update_args.add_argument("name", type=str, help="Name of the book is required")
book_update_args.add_argument("author", type=str, help="Author of the book is required")
book_update_args.add_argument("narrator", type=str, help="Name of the book is required")
book_update_args.add_argument("duration", type=int, help="Duration of the book is required")
book_update_args.add_argument("uploaded_time", type=str, help="Time of upload for book is required")

def handle_bad_request_with_header(error):
    '''This is a custom error'''
    return {'message': 'The requrst is invalid'}, 500

#Resource_fields for Song table
resource_fields_songs = {
	'id': fields.Integer,
	'name': fields.String,
	'duration': fields.Integer,
	'uploaded_time': fields.String
}

#Resource_fields for Book table
resource_fields_book = {
	'id': fields.Integer,
	'name': fields.String,
	'author': fields.String,
	'narrator': fields.String,
	'duration': fields.Integer,
	'uploaded_time': fields.String
}

#Resource_fields for Pod table
resource_fields_pod = {
	'id': fields.Integer,
	'name': fields.String,
	'duration': fields.Integer,
	'uploaded_time': fields.String,
	'host' : fields.String,
	'participants' : fields.String
}

class Audio(Resource):

#GET Method
	def get(self, filetype, audio_id):
		#print("I am in get model")
		if filetype == "song":
			#print("I am in song if")
			result = SongModel.query.filter_by(id=audio_id).first()
			#audio = SongModel(id=audio_id, name=args['name'], duration=args['duration'], uploaded_time=args['uploaded_time'])
			value = resource_fields_songs 
		elif filetype == "audiobook":
			#print("I am in book if")
			result = AudioBookModel.query.filter_by(id=audio_id).first()
			value = resource_fields_book
		else:
			#print("I am in pod if")
			result = PodcastModel.query.filter_by(id=audio_id).first()
			value = resource_fields_pod
		if not result:
			abort(400, message="The request is invalid")
		handle_bad_request_with_header(result)
		return marshal(result, value, 'Action is Successful'), 200

#PUT method
	def put(self, filetype, audio_id):
		print("I am in put menthod")
		if filetype == "song":
			args = song_put_args.parse_args()
			result = SongModel.query.filter_by(id=audio_id).first()
			if result:
				abort(409, message="Audio id taken...")
			audio = SongModel(id=audio_id, name=args['name'], duration=args['duration'], uploaded_time=args['uploaded_time'])
			value = resource_fields_songs 
		elif filetype == "audiobook":
			args = book_put_args.parse_args()
			result = AudioBookModel.query.filter_by(id=audio_id).first()
			print(type(result))
			if result:
				abort(409, message="Audio id taken...")
			print(" i am in book else")
			audio = AudioBookModel(id=audio_id, name=args['name'],  author=args['author'],  narrator=args['narrator'], duration=args['duration'], uploaded_time=args['uploaded_time'])
			value = resource_fields_book
		else:
			print(" I am in podcast")
			result = PodcastModel.query.filter_by(id=audio_id).first()
			args = pod_put_args.parse_args()
			if result:
				abort(409, message="Audio id taken...")
			audio = PodcastModel(id=audio_id, name=args['name'], duration=args['duration'], uploaded_time=args['uploaded_time'], host=args['host'], participants= args['participants'])
			value = resource_fields_pod

		db.session.add(audio)
		db.session.commit()
		return marshal(audio, value), 201

#Patch Method
	def patch(self, filetype, audio_id):
		if filetype == "song":
			args = song_update_args.parse_args()
			result = SongModel.query.filter_by(id=audio_id).first()
			if not result:
				abort(400, message="The request is invalid")
			if args['name']:
				result.name = args['name']
			if args['duration']:
				result.duration = args['duration']
			if args['uploaded_time']:
				result.uploaded_time = args['uploaded_time']
			value = resource_fields_songs
		elif filetype == "audiobook":
			args = book_update_args.parse_args()
			result = AudioBookModel.query.filter_by(id=audio_id).first()
			if not result:
				abort(400, message="The request is invalid")
			handle_bad_request_with_header(result)
			if args['name']:
				result.name = args['name']
			if args['author']:
				result.author = args['author']
			if args['narrator']:
				result.narrator = args['narrator']
			if args['duration']:
				result.duration = args['duration']
			if args['uploaded_time']:
				result.uploaded_time = args['uploaded_time']
			value = resource_fields_book
		else:
			args = pod_update_args.parse_args()
			result = PodcastModel.query.filter_by(id=audio_id).first()
			if not result:
				abort(400, message="The request is invalid")

			if args['name']:
				result.name = args['name']
			if args['duration']:
				result.views = args['duration']
			if args['uploaded_time']:
				result.likes = args['uploaded_time']
			if args['host']:
				result.host = args['host']
			if args['participants']:
				result.participants = args['participants']
			value = resource_fields_pod

		db.session.commit()

		return marshal(result, value, 'Action is successful'), 201


#DELETE Method
	def delete(self, filetype, audio_id):
		print("I am in delete method")
		#abort_if_audio_id_doesnt_exist(audio_id)
		#del songs[audio_id]
		if filetype == "song":
			result = SongModel.query.filter_by(id=audio_id).first()
		elif filetype == "audiobook":
			result = AudioBookModel.query.filter_by(id=audio_id).first()
		else:
			result = PodcastModel.query.filter_by(id=audio_id).first()
		#record_obj = db.session.query(SongModel).filter(SongModel.id==audio_id).first()
		db.session.delete(result)
		db.session.commit()
		#query = models.SongModel.delete().where(models.SongModel.id==audio_id)
		#query.execute()
		return '', 204

#Add resource
api.add_resource(Audio, "/<string:filetype>/<int:audio_id>")

if __name__ == "__main__":
	app.run(debug=True)