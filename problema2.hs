-- Problema 2
verificarContrasena :: String -> String -> String
verificarContrasena guardada ingreso =
    if map toLower guardada == map toLower ingreso
       then "Contraseña correcta"
       else "Contraseña incorrecta"
  where toLower c = if c >= 'A' && c <= 'Z' then toEnum (fromEnum c + 32) else c
