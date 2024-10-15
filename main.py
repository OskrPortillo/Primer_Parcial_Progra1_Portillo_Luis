from UTN_Heroes_Dataset.utn_pp import get_original_matrix
from app_menu import concesionaria_app


matriz_concesionaria = get_original_matrix()

if __name__ == '__main__':

    concesionaria_app(matriz_concesionaria)