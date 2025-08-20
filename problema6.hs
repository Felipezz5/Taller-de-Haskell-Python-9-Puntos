-- Problema 6
asignacion :: String -> String -> String
asignacion nombre genero
    | map toLower genero == "f" = nombre ++ " está en el Grupo A"
    | map toLower genero == "m" = nombre ++ " está en el Grupo B"
    | otherwise = nombre ++ " está en el Grupo C"
  where toLower c = if c >= 'A' && c <= 'Z' then toEnum (fromEnum c + 32) else c