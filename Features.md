### Features
✅ Un usuario puede registrarse introduciendo su email y eligiendo un nombre de usuario libre y una contraseña
✅ Un usuario debe ser capaz de logarse utilizando email y contraseña.
✅ Un usuario debe poder cambiar su contraseña.
✅ Un usuario debe poder restaurar su contraseña recibiendo un email con un magic link.
✅ Un usuario puede publicar una idea como un texto corto en cualquier momento.
✅ Un usuario puede establecer la visibilidad de una idea: publica (todos pueden verla), protegida (solo otros usuarios que siguen al usuario de la idea pueden verla) y privada (solo el usuario que creó la idea puede verla)
✅ Un usuario puede establecer la visibilidad de una idea en el momento de su creacion o editarla posteriormente.
✅ Un usuario puede consultar todas las ideas que ha publicado ordenadas de mas recientes a mas antiguas.
✅ Un usuario puede borrar una idea publicada.
✅ Un usuario puede solicitar seguir a otro usuario
✅ Un usuario puede ver el listado de solicitudes de seguimiento recibidas y aprovarlas o denegarlas
✅ Un usuario puede ver el listado de gente a la que sigue
✅ Un usuario puede ver el listado de gente que le sigue
✅ Un usuario puede dejar de seguir a alguien
✅ Un usuario puede eliminar a otro usuario de su lista de seguidores
✅ Un usuario puede realizar una busqueda de otros usuarios introduciendo un nombre de usuario o parte de uno
✅ Un usuario puede ver la lista de ideas de cualquier otro usuario, teniendo en cuenta la visibilidad de cada idea.
✅ Un usuario puede ver un timeline de ideas compuesto por sus propias ideas y las ideas de los usuarios a los que sigue, teniendo en cuenta la visibilidad de cada idea.
✅ El proyecto debe incluir lo necesario para levantar un entorno de desarrollo que provea de las dependencias necesarias y de la base de datos. Se puede utilizar docker, Vagrant...
✅ El proyecto debe incluir un README.md con instrucciones para levantar el entorno de desarrollo y todas las consideraciones que se crean oportunas.
- Un usuario debe recibir una notificación cada vez que un usuario al que sigue publica una idea nueva a la que tiene acceso (https://github.com/jazzband/django-push-notifications)

### TODO:
- Uso de servicios de terceros (envio de email, notificaciones push, etc...).
- Tests
- Custom Exceptions:
    - Not logged in exception.
    - Bad user exception.
- Si eres administrador, devolver todas las ideas, independiente del id de los usuarios o de su visiblidad.
- Si eres administrador, puedes editar cualquier idea, independientemente de su dueño.
- Comprobar si el campo visibility de una Idea puede ser de tipo Visibility directamente y no un CharField
- No permitir login si la cuenta está por verificar