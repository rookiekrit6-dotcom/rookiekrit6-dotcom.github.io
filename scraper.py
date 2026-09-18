import json
from datetime import datetime

def update_savings_data():
    filename = 'accounts.json'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"last_updated": "", "accounts": []}
    
    # อัปเดตวันที่เป็นวันปัจจุบันอัตโนมัติ
    current_date = datetime.now().strftime('%Y-%m-%d')
    data['last_updated'] = current_date
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully updated date in {filename} to {current_date}")

if __name__ == '__main__':
    update_savings_data()
