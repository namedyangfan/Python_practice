############ writing HGS commends for making SK observation wells
from write_obs_wells import write_obs_coord
import unittest
## give the abs path for the ND well data

parms = {"file_name":"ND_wells_utm.csv", 
		"file_path" : r".\test",
		"save_path" : r".\test",
		"save_name" : "make_obs_wells.inc"}

class write_obs_coord_TestCase(unittest.TestCase):

	global parms

	def test_read_coordf(self):
		t = write_obs_coord( 	file_name = parms["file_name"], 
								file_path = parms["file_path"], 
								save_file_name = parms["save_name"], 
								save_file_path = parms["save_path"], 
								layer_num_start = 1, 
								layer_num_end = 6)
		try:
			t.readfile()
		except:
			self.fail('unable to read file {}'.format(t.summary_file))

	def test_write_file(self):
		t = write_obs_coord( 	file_name = parms["file_name"], 
							file_path = parms["file_path"], 
							save_file_name = parms["save_name"], 
							save_file_path = parms["save_path"], 
							layer_num_start = 1, 
							layer_num_end = 6)
		
		t.readfile()
	
		try:
			t.write_hgs()
		except:
			self.fail('unable to write file {}'.format(t.save_file_name))


if __name__ == '__main__':
    unittest.main()

# ##read coordinates of wells to data.frame
# sk.readfile()
# ##write observation wells
# sk.write_hgs()