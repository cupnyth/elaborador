import win32com.client
import os

class Digitalize:
    def __init__(self):
        self.scan_path = "scaneados"
        self.exames_path = "exames"
        os.makedirs(self.scan_path,exist_ok=True)
        os.makedirs(self.exames_path,exist_ok=True)

    def digitalizar(self, nome_arquivo: str, sub_path="Unanamed"):
        try:
            caminho_completo = os.path.join(os.getcwd(), fr"{self.scan_path}\{sub_path}", nome_arquivo)
            print(f"Tentando salvar em: {caminho_completo}")

            diretorio = os.path.dirname(caminho_completo)
            if diretorio and not os.path.exists(diretorio):
                try:
                    os.makedirs(diretorio)
                    print(f"Diretório {diretorio} criado com sucesso.")
                except Exception as e:
                    print(f"Erro ao criar diretório {diretorio}: {e}")
                    return False

            try:
                with open(caminho_completo, 'wb') as teste:
                    pass  
                os.remove(caminho_completo)  
                print(f"Caminho {caminho_completo} é válido para escrita.")
            except Exception as e:
                print(f"Erro ao verificar caminho {caminho_completo}: {e}")
                return False

            wia = win32com.client.Dispatch("WIA.DeviceManager")
            if not wia.DeviceInfos.Count:
                print("Erro: Nenhum scanner encontrado.")
                return False

            dispositivo = wia.DeviceInfos.Item(1).Connect()
            if not dispositivo:
                print("Erro: Não foi possível conectar ao scanner.")
                return False

            item = dispositivo.Items.Item(1)
            
            try:
                item.Properties("Current Intent").Value = 1  
            except Exception as e:
                print(f"Aviso: Não foi possível definir modo de cor. Usando padrão. ({e})")

            imagem = item.Transfer()
            if not imagem:
                print("Erro: Falha ao transferir imagem.")
                return False

            imagem.SaveFile(caminho_completo)
            print(f"Imagem digitalizada salva como {caminho_completo}")
            return caminho_completo

        except Exception as e:
            print(f"Erro durante a digitalização com WIA: {e}")
            return False
        finally:
            if 'dispositivo' in locals():
                dispositivo = None
            if 'wia' in locals():
                wia = None


if __name__ == "__main__":
    dj = Digitalize()
    dj.digitalizar("teste.jpg")