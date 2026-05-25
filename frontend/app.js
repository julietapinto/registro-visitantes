const API = "https://registro-visitantes-wt8j.onrender.com";

const formulario = document.getElementById("formulario");
const tabla = document.getElementById("tablaVisitantes");

async function cargarVisitantes() {

    const respuesta = await fetch(`${API}/visitantes`);
    const visitantes = await respuesta.json();

    tabla.innerHTML = "";

    visitantes.forEach(v => {

        tabla.innerHTML += `
            <tr>
                <td>${v.nombre}</td>
                <td>${v.identificacion}</td>
                <td>${v.motivo}</td>
            </tr>
        `;
    });
}

formulario.addEventListener("submit", async (e) => {

    e.preventDefault();

    const visitante = {
        nombre: document.getElementById("nombre").value,
        identificacion: document.getElementById("identificacion").value,
        motivo: document.getElementById("motivo").value
    };

    await fetch(`${API}/visitantes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(visitante)
    });

    formulario.reset();

    cargarVisitantes();
});

cargarVisitantes();