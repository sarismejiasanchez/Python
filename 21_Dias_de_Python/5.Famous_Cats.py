'''
Encuentra a los gatitos más famosos

En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:

"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, manteniendo el orden en el que aparecen en la lista de entrada.
'''
def find_famous_cat(cats):
  max_followers = 0
  famous_cats = []
  
  for cat in cats:
    
    followers = cat["followers"]
    total_followers = sum(followers)
    #print (cat["name"], total_followers)
    
    if total_followers > max_followers:
      max_followers = total_followers
      famous_cats = [cat["name"]]
    elif total_followers == max_followers:
      famous_cats.append(cat["name"])
      
  return famous_cats
  
test = find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

print(test)

test = find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])

print(test)