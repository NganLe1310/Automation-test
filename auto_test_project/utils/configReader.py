import json
import os
 
class ImportJson:
    @staticmethod
    def read_credentials(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Không tìm thấy file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data.get("username"), data.get("password")
            except json.JSONDecodeError as e:
                raise ValueError(f"Lỗi khi đọc file JSON: {e}")
            