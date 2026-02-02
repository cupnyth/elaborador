from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import select, text
from src.db.models import Empresa, Pending
import os
from dotenv import load_dotenv
import logging

logger = logging.Logger("Database")

class Database:
    def __init__(self):
        # Carrega o .env
        load_dotenv()

        # 1. Busca as variáveis com os SEUS nomes personalizados
        db_host = os.getenv("DB_HOSTPENDING")
        db_port = os.getenv("DB_PORTPENDING")
        db_user = os.getenv("DB_USERPENDING")
        db_pass = os.getenv("DB_PASSWORDPENDING")
        db_name = os.getenv("DB_NAMEPENDING")

        # Validação básica para não bater cabeça com erro estranho
        if not all([db_host, db_port, db_user, db_pass, db_name]):
            print("❌ [ERRO ELABORADOR] Faltam variáveis no arquivo .env!")
            # Opcional: Levantar erro ou usar valores padrão (não recomendado para produção)

        # 2. Monta a string de conexão Dinâmica
        _database_sinc = (
            f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        )
        
        # 3. Cria o Engine
        self.__engine = create_engine(
            _database_sinc,
            echo=False,
            future=True
        )
        
        self.session = sessionmaker(
            bind=self.__engine,
            class_=Session,
            expire_on_commit=False
        )

    def get_all_companies(self):
        with self.session() as session:
            _select_ = select(Empresa)
            result = session.execute(_select_).scalars().all()
            session.close()
            return result

    def concluir_exame(self, nome_paciente: str, nome_empresa: str, caminho_pdf: str):
        """
        Busca exames pendentes desse paciente nessa empresa e marca como Concluido.
        """
        try:
            with self.session() as session:
                # SQL direto para garantir joins corretos
                sql = text("""
                    UPDATE pending
                    SET status = 'Concluido',
                        link_pdf = :pdf
                    WHERE id IN (
                        SELECT e.id
                        FROM pending e
                        JOIN pacientes p ON e.paciente_id = p.id
                        JOIN empresas emp ON p.empresa_id = emp.id
                        WHERE p.nome = :paciente
                          AND emp.nome = :empresa
                          AND e.status IN ('Pendente', 'Em andamento')
                    )
                """)
                
                result = session.execute(sql, {
                    "pdf": caminho_pdf, 
                    "paciente": nome_paciente, 
                    "empresa": nome_empresa
                })
                session.commit()
                
                linhas = result.rowcount
                if linhas > 0:
                    print(f"✅ [SUCESSO] {linhas} exame(s) atualizado(s) no Portal!")
                    return True
                else:
                    print("⚠️ [AVISO] Nenhum exame pendente encontrado no Portal.")
                    return False
                    
        except Exception as e:
            print(f"❌ [ERRO DB] Falha ao atualizar Portal: {e}")
            return False