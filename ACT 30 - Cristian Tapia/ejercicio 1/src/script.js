const ENDPOINT_PRODUCTOS = 'https://dummyjson.com/products?limit=12';

const contenedorMosaico = document.getElementById('mosaico-productos');
const textoCarga = document.getElementById('indicador-carga');
const mensajeError = document.getElementById('caja-error');

function cargarCatalogo() {
  fetch(ENDPOINT_PRODUCTOS)
    .then(res => {
      if (!res.ok) {
        throw new Error('No se pudo establecer conexión con el servidor.');
      }
      return res.json();
    })
    .then(datos => {
      if (textoCarga) textoCarga.classList.add('ocultar');
      desplegarItems(datos.products);
    })
    .catch(err => {
      if (textoCarga) textoCarga.classList.add('oculto');
      if (mensajeError) {
        mensajeError.textContent = 'Ocurrió un inconveniente al cargar los artículos.';
        mensajeError.classList.remove('ocultar');
      }
      console.error('Detalle del error:', err);
    });
}

function desplegarItems(lista) {
  if (!contenedorMosaico) return;

  lista.forEach(item => {
    const bloqueCard = document.createElement('article');
    bloqueCard.className = 'tarjeta-item';
    
    bloqueCard.innerHTML = `
      <img src="${item.thumbnail}" alt="${item.title}">
      <h4>${item.title}</h4>
      <span class="etiqueta-precio">$${item.price.toFixed(2)}</span>
    `;

    contenedorMosaico.appendChild(bloqueCard);
  });
}

cargarCatalogo();