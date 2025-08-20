-- Problema 9
pizza :: Bool -> String -> String
pizza vegetariana ingrediente
    | vegetariana = "Pizza vegetariana con mozzarella, tomate y " ++ ingrediente
    | otherwise   = "Pizza no vegetariana con mozzarella, tomate y " ++ ingrediente
