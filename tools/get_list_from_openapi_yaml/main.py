import yaml
import pandas as pd
import os

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def extract_paths_and_methods(openapi_data, file_name):
    paths_data = openapi_data.get('paths', {})
    path_list = []
    for path, methods in paths_data.items():
        for method in methods.keys():
            path_list.append({'file': file_name, 'path': path, 'method': method})
    return path_list

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

def main(input_folder, output_excel_file):
    all_path_method_list = []
    yaml_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.yaml')]
    for yaml_file in yaml_files:
        openapi_data = load_yaml(yaml_file)
        path_method_list = extract_paths_and_methods(openapi_data, os.path.basename(yaml_file))
        all_path_method_list.extend(path_method_list)
    save_to_excel(all_path_method_list, f"output/{output_excel_file}")
    print(f"Exported as output/{output_excel_file}")

if __name__ == '__main__':
    main('input', 'combined_paths_and_methods.xlsx')