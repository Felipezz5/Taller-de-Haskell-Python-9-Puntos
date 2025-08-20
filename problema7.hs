-- Problema 7
evaluarEmpleado :: Int -> String
evaluarEmpleado p
    | p >= 10 = "Excelente, recibe $200000"
    | p >= 7 = "Bueno, recibe $100000"
    | p >= 5 = "Aceptable, recibe $50000"
    | otherwise = "Pongase a trabajar, no recibe recompensa"