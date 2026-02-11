import sys
import io
from PIL import Image


def salvar_imagem(imagem, tamanho_maximo = (800, 800)):

    if not imagem:
        return

    caminho = imagem.path

    with Image.open(caminho) as img:    

        if img.width > tamanho_maximo[0] or img.height > tamanho_maximo[1]:
            img.thumbnail(tamanho_maximo, Image.Resampling.LANCZOS)            

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(caminho, optimize=True, quality=85)
