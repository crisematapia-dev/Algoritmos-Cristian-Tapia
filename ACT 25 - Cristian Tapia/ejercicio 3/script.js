function cargarPilotos() {
  const pilotos = [];
  
  for (let i = 0; i < 4; i++) {
    const nombre = prompt(`Ingrese el nombre del piloto n° ${i + 1}:`);
    const vue1 = parseFloat(prompt(`Ingrese el tiempo de la 1° vuelta de ${nombre}:`));
    const vue2 = parseFloat(prompt(`Ingrese el tiempo de la 2° vuelta de ${nombre}:`));
    const vue3 = parseFloat(prompt(`Ingrese el tiempo de la 3° vuelta de ${nombre}:`));
    
    pilotos.push([nombre, [vue1, vue2, vue3]]);
  }
  
  return pilotos;
}

// 2. Calcular Promedios
function calcularPromedios(pilotos) {
  console.log("Promedio de tiempo por piloto");
  
  for (const [nombre, tiempos] of pilotos) {
    let suma = 0;
    for (const tiempo of tiempos) {
      suma += tiempo;
    }
    const promedio = suma / tiempos.length;
    console.log(`El piloto ${nombre} tiene un tiempo promedio de: ${promedio.toFixed(2)}s`);
  }
}


function mejorVuelta(pilotos) {
  console.log("Mejor Vuelta");
  

  let mejorTiempo = pilotos[0][1][0]; 
  let mejorPiloto = pilotos[0][0];

  for (const [nombre, tiempos] of pilotos) {
    for (const tiempo of tiempos) {
      if (tiempo < mejorTiempo) {
        mejorTiempo = tiempo;
        mejorPiloto = nombre;
      }
    }
  }

  console.log(`La vuelta más rápida fue de ${mejorPiloto}, con un tiempo de: ${mejorTiempo}s`);
}

// Bloque Principal
function bloquePrincipal() {
  const pilotos = cargarPilotos();
  calcularPromedios(pilotos);
  mejorVuelta(pilotos);
}

bloquePrincipal();