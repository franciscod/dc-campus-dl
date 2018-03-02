import Data.Char

type Gen = Char
type Rasgo = [Char]
type Dominacion = Integer
type Alelo = (Gen, Rasgo, Dominacion)

-- DATASET de Aelos de la arveja
alelosArveja :: [Alelo]
alelosArveja = [('R',"Semilla Lisa", 1),('R',"Semilla Rugosa",2),
                  ('Y',"Semilla Amarilla",1),('Y',"Semilla Verde",0),
                  ('P',"Flor Purpura",4),('P',"Flor Blanca",3),
                  ('I',"Legumbre Lisa",2),('I',"Legumbre Estrangulada",1),
                  ('G',"Legumbre Verde",0),('G',"Legumbre Amarilla",4),
                  ('A',"Flor Axial",3),('A',"Flor Terminal",0),
                  ('T',"Tallo Normal",2),('T',"Tallo Enano",1)]

type Set a = [a]
type Genotipo = Set Alelo

