## ¿Por qué existe esta versión?

Existe porque la barra hace algo que
no es lo que espero. Cuando el texto
alcanza el límite derecho no tiene
que verse como si se hubiera creado
una página nueva con el cursor al
final, tiene que verse como si el
texto simplemente hubiera seguido
y ya.

# edit

Existe porque en el `redraw()` no se
tiene en cuenta la posición de la `e`
como parte de la ecuación.

## Causas puntuales

_Slicing incorrecto_
_e no es parte de la ecuación_
