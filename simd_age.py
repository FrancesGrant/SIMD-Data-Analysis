# Import Statements
import csv
from os.path import exists


def skip_lines(file_connection, x):
	""" Function to skip a number of lines."""
	for i in range(x):
		file_connection.readline()

class CensusData:
	# Constructor class
	def __init__(self, filename):
		self.filename = filename
		self.data_dict= {}

	# Data Representation for ouptut
	def __repr__(self):
		rep = 'Census Data, from file: ' + str(self.filename) + " : " + str(self.data_dict)
		return rep

	def load(self):
		""" Function to load the dataset."""
		#  Check if input file exists
		if exists(self.filename):
			openFile = open(self.filename, 'r', encoding='iso-8859-1')
			skip_lines(openFile, 4)
			dictionaryReading = csv.DictReader(openFile)
			for row in dictionaryReading:
				if row['Region'] in self.data_dict.keys():
					self.data_dict[row['Region']][row['Range']] = row['All people']
				else:
					self.data_dict[row['Region']] = {row['Range'] : row['All people']}
			return True
		else:
			return False

	def regions(self):
		""" Function that generates a list of available regions in the dataset"""
		areas = []
		for key in self.data_dict:
			if not key in areas: 
				areas.append(key)			
		return areas

	def total_population(self, region, age):
		""" Function that calculates the popoulation in a specifix region =< age"""
		population = 0
		areas = self.regions()
		if region in areas:
			sub_dict = self.data_dict[region]
			population += int(sub_dict['Under 1'])
			if age == 'Under 1':
				return population
			for i in range(1, age + 1):
				print(i)
				population += int(sub_dict[str(i)])
			if age == '85 to 89':
				population += int(self.data_dict[region]['85 to 89'])
				return population
			elif age == '90 to 94':
				population += int(self.data_dict[region]['85 to 89'])
				population += int(self.data_dict[region]['90 to 94'])
				return population
			elif age == '95 and over':
				population += int(self.data_dict[region]['85 to 89'])
				population += int(self.data_dict[region]['90 to 94'])
				population += int(self.data_dict[region]['95 and over'])
				return population
			else:
				return population


class SIMD_Data:
	# Constructor class
	def __init__(self, filename):
		self.filename = filename
		self.data_dict = {}

	# Data Representation for ouptut
	def __repr__(self) -> str:
		rep = 'file' + self.filename + " data_dict " + str(self.data_dict)
		return rep 

	def load(self):
		""" Function to load the dataset."""
		if exists(self.filename):
			openFile = open(self.filename, 'r', encoding='iso-8859-1')
			dictionaryReading = csv.DictReader(openFile)
			for row in dictionaryReading:
				self.data_dict[row["MMWname"]] = row['SIMD2020v2_Rank']
			return True 
		else:
			return False

	def regions(self):
		""" Function that returns a list of regions that have been loaded"""
		areas = []
		for key in self.data_dict:
			if not key in areas: 
				areas.append(key)			
		return areas
	

	def lowest_simd(self):
		""" Function that returns the name of the region with the lowest SIMD rank"""
		areas = self.regions()
		lowest = self.data_dict[areas[0]]
		self.lowest_area = areas[0]
		for i in range(1, len(areas)):
			if self.data_dict[areas[i]] < lowest:
				lowest = str(self.data_dict[areas[i]])
				lowest_area = str(areas[i])
		return lowest_area
		
# Main function that calls when SIMD_age.py file is executed
def main():
	census_data = CensusData("DC1117SC.csv")
	census_data.load()
	census_data.regions()
	
	simd_data = SIMD_Data("SIMD_2020v2.csv")
	simd_data.load()
	simd_data.regions()

	print (simd_data.lowest_simd())
	len(census_data.regions())
	region = simd_data.lowest_area
	
	region_score = simd_data.data_dict[region]

	print('The Region with the lowest average SIMD score is:' + region)
	print('This areas has an average SIMD score of:' + region_score)
	
	under_15 = census_data.total_population(region, 15)

	print(region + " has a population of: " + str(under_15) + " Aged 15 or under")
  
if __name__ == "__main__":
	main()


