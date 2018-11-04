import peewee
from .readerfactory import ReaderFactory
from . import model
import os

class Importer:
	'''
	Import a supported filename into sqlite database 
	'''
	def __init__(self, db_filename):
		self.db_filename = db_filename



	def import_file(self, filename):

		# Init database
		self.database = peewee.SqliteDatabase(self.db_filename)
		model.db.initialize(self.database)

		os.remove(self.db_filename)
		# Create table 
		self.database.create_tables([
			model.Variant,
			model.Field])

		model.Field.insert_default()


		# depend on file type.. Actually, only one 
		reader = ReaderFactory.create_reader(filename)

	
		with self.database.atomic():
			chunk_size = 100
			chunk = []
			for i in reader.get_variants():
				chunk.append(i)

				if len(chunk)  == chunk_size:
					model.Variant.insert_many(chunk).execute()
					chunk.clear()


			model.Variant.insert_many(chunk).execute()




				




		