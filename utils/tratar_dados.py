from pathlib import Path
import pandas as pd

def to_lower_case(header_list: list) -> list:
    fixed_header = []
    
    for header in header_list:
        fixed_header.append(header.lower())
    
    return fixed_header

def remove_dash_and_underscore(header_list: list) -> list:
    fixed_header = []
    
    for header in header_list:
        fixed_header.append(header.replace("/", "_"))
    
    return fixed_header

def remove_blank_space(header_list: list) -> list:
    fixed_header = []
    
    for header in header_list:
        fixed_header.append(header.replace(" ", "_"))
    
    return fixed_header

def fix_header_to_standarts(header_list: list) -> list:
    header_list = to_lower_case(header_list)
    header_list = remove_dash_and_underscore(header_list)
    header_list = remove_blank_space(header_list)
    return header_list

def file_origin(option:int) -> None:
    if option == 1:
        format = "csv"
        
    else:
        format = "pkl"
        
    print(f"Read from .{format} file format")

def read_data(dataset_path:str, dir='databases'):
    db_path = Path(f'{dir}/{dataset_path}')

    dir_path = db_path.parent
    raw_filename = db_path.parent / 'raw' / db_path.with_suffix('.csv').name
    proc_filename = db_path.parent / 'processed' / db_path.with_suffix('.pkl').name

    if proc_filename.exists():
        file_origin(2)
        return pd.read_pickle(proc_filename)
    
    else:
        file_origin(2)
        frame = pd.read_csv(raw_filename)
        # tratamento dos dados (Nulos, Conversões, Pradronizações)
        frame.to_pickle(proc_filename)
        return frame