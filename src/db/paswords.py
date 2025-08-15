import json
import os 
class Passwords:
    def __init__(self):
        os.makedirs(r"src\db\encrypt",exist_ok=True)
        self.create_json()

    def create_json(self):
        dados = {}
        if not os.path.exists(r"src\db\encrypt\companies.json"):
            with open(r"src\db\encrypt\companies.json","w",encoding="utf-8") as f:
                json.dump(dados,f,indent=4,ensure_ascii=False)
    
    def set_companies(self,enterprise,password):
        with open(r"src\db\encrypt\companies.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
        dados[enterprise] = password
        with open(r"src\db\encrypt\companies.json","w",encoding="utf-8") as f:
            json.dump(dados,f,indent=4,ensure_ascii=False)

    def get_companiesKey(self,enterprise) -> str | None:
        try:
            with open(r"src\db\encrypt\companies.json", "r",encoding="utf-8") as f:
                dados = json.load(f)
            return dados[enterprise]
        except:
            return None
        
            
    