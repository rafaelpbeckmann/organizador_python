import os
caminhos = r"C:\Users\rafae\Downloads"
pastas_objetivo = {
    ".pdf": "arquivos_pdf",
    ".docx": "arquivos_docx",
    ".xlsx": "planilhas",
    ".jpg": "imagens",
    ".png": "imagens",
    ".zip": "arquivos_comprimidos",
    ".rar": "arquivos_comprimidos",
    ".iso": "arquivos_comprimidos",
    ".exe": "executaveis",
    ".pptx": "apresentacoes",
    ".jpeg": "imagens",
    ".gif": "imagens",
    ".ppt": "apresentacoes",
}
arquivos = os.listdir(caminhos)
for arquivo in arquivos:
    nome_arquivo, extensao = os.path.splitext(arquivo)
    pasta_destino = pastas_objetivo.get(extensao, "outros")
    caminho_completo_pasta = os.path.join(caminhos, pasta_destino)
    print(f"Arquivo: {arquivo} | Destino: {caminho_completo_pasta}")
    if not os.path.exists(caminho_completo_pasta):
        os.makedirs(caminho_completo_pasta)
    caminho_antigo_arquivo = os.path.join(caminhos, arquivo)
    caminho_novo_arquivo = os.path.join(caminho_completo_pasta, arquivo)
    os.rename(caminho_antigo_arquivo, caminho_novo_arquivo)    