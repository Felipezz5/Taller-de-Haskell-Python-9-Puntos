-- Problema 5
impuestos :: Int -> Float -> String
impuestos edad ingresos =
    if edad >= 18 && ingresos >= 160232000
       then "Debe pagar impuesto de renta"
       else "No debe pagar impuesto de renta"