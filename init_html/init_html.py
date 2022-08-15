
import os
from rich import print

os.system("cls")
# Création du dossier entrez par l'utilisateur
saisie_folder = input('Veuillez entrez le nom de votre projet >')
os.mkdir(f"project/{saisie_folder}");
    
# Création du fichier qui portera par défaut le nom index.html
open(f"project/{saisie_folder}/index.html", "w+")

# Creation du dossier css qui aura un style.css
os.mkdir(f'project/{saisie_folder}/style')
open(f"project/{saisie_folder}/style/styles.css", "w+")


# Création du dossier js contenant un fichier index.js 
os.mkdir(f'project/{saisie_folder}/JS') 
open(f"project/{saisie_folder}/JS/index.js", "w+")


# On écrit dans le fichier html le templates par défaut.
template_html_default = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- CSS DEFAULT -->
    <link rel="stylesheet" href="./style/styles.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
     <!-- CSS DEFAULT -->
    <title>troc</title>
</head>
<body>
    <!-- As a link -->
    <nav class="navbar bg-dark text-info">
      <div class="container">
      <a class="navbar-brand text-info" href="#">{saisie_folder}</a>
    </div>
    </nav>
    <div class="container">
      <h1></h1>
      <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h1 class="display-4">Votre projet <span class="text-success">{saisie_folder}</span> est pret !</h1> 
        <p class="lead">Nous vous remercions d'avoir utiliser notre outil, modifier le fichier 'index.html', notre outil utilise le CDN <span class="text-info text-bg-light fw-bold">'Bootstrap'</span>.</p>
      </div>

   
    
    </div>
    
    <footer class=" my-md-5 p-2 md-5 border-top bg-dark">
      <script src="./JS/index.js"></script>
        <div class="row">
          <div class="col-12 col-md">
            <p class="text-info fw-bolder">{saisie_folder}</p>
            <small class="d-block mb-3 text-muted">2019-2020</small>
          </div>
          <div class="col-6 col-md">
            <h5 class="text-info fw-bolder">NOS SERVICES</h5>
            <ul class="list-unstyled text-small">
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Cool stuff</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Random feature</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Team feature</a></li>
              
            </ul>
          </div>
          <div class="col-6 col-md">
            <h5 class="text-info fw-bolder">RESSOURCE</h5>
            <ul class="list-unstyled text-small">
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Resource</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Resource name</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Another resource</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Final resource</a></li>
            </ul>
          </div>
          <div class="col-6 col-md">
            <h5 class="text- fw-bolder">A PROPOS</h5>
            <ul class="list-unstyled text-small">
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Team</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Locations</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Privacy</a></li>
              <li><a class="text-info text-decoration-none fw-lighter" href="#">Terms</a></li>
            </ul>
          </div>
        </div>
    </footer>
    
</body>
</html> 
"""
fichier_html = open(f'project/{saisie_folder}/index.html',"w")
fichier_html.write(template_html_default);
fichier_html.close()

# On ecrit dans le fichier css 
style_template_default = """""" 
fichier_css = open(f'project/{saisie_folder}/style/styles.css',"w")
fichier_css.write(style_template_default)
fichier_css.close()
print("Projet initialiser avec succées")
print(f"Votre projet se situe dans 'project/{saisie_folder}' ")





