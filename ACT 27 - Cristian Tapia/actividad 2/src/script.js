/*2. Cargar un nombre y un apellido en dos text. Al presionar un botón,
concatenarlos y mostrarlos en un tercer text (Tener en cuenta que
podemos modificar la propiedad value de un objeto TEXT cuando ocurre
un evento).*/
function mostrar() {
    let texto3 = document.getElementById('usuario').value;
    let nom = document.getElementById('nombre').value;
    let ed = document.getElementById('apellido').value;
    texto3=('nombre del usuario : ' + nom + ed )
    print(texto3)
}