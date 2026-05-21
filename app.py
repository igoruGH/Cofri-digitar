import os

def conectar_banco():
    print("Iniciando sistema do Cofre Digital...")
    
    # O "os.getenv" é a nossa fechadura. Ele procura a senha no ambiente do computador, não no código!
    usuario = os.getenv("USUARIO_BANCO", "usuario_padrao")
    senha = os.getenv("SENHA_BANCO", "SENHA_NAO_CONFIGURADA")
    
    # Simulando a máscara de log (Protegendo "a visão de curiosos no terminal)
    if senha != "SENHA_NAO_CONFIGURADA" and len(senha) > 4:
        senha_mascarada = senha[:2] + "****" + senha[-2:]
    else:
        senha_mascarada = "****"

    print(f"Tentando conectar com o usuário: {usuario}")
    
    # NUNCA dê 'print' na variável 'senha' original! Imprima apenas a versão mascarada.
    print(f"Senha utilizada (mascarada nos logs): {senha_mascarada}")
    
    if senha == "SENHA_NAO_CONFIGURADA":
        print("ERRO: Acesso negado. A fechadura está trancada.")
    else:
        print("SUCESSO: Conectado ao banco de dados secreto!")

if __name__ == "__main__":
    conectar_banco()
    