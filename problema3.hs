-- Problema 3
division :: Float -> Float -> String
division _ 0 = "No se puede dividir por cero"
division a b = "Resultado: " ++ show (a / b)