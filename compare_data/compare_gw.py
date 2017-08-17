from convert_tecplot import hgs_loadfile as hl
import os, errno

def gwl_to_depth(df):
    pass

if __name__ == "__main__":
    file_directory = r'./test_data'
    file_name = 'Riceton.dat'
    file_path = os.path.join(file_directory, file_name)
    df = hl.read_tecplot(file_directory=file_directory, file_name=file_name, sep='\s')
    print(df.head(10))

    df.to_csv("test",index=None)


