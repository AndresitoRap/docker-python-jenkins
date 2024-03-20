html_content="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>Python Docker</title>
  </head>
  <body>
    <h1>¡Hola mundo sin flask desde un docker!</h1>
  </body>
</html>
"""

with open ("hola_mundo .html", "w") as file:
    file.write(html_content)    

print("Se creo el html hola mundo.")