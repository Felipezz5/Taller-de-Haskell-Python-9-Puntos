-- Problema 8
precioArcade :: Int -> String
precioArcade edad
    | edad < 12 = "Precio del ticket: $6000"
    | edad < 18 = "Precio del ticket: $9000"
    | edad < 65 = "Precio del ticket: $13000"
    | otherwise = "Precio del ticket: $7000"