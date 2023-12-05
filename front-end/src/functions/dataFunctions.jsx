import { useEffect } from "react";


export function GraphCommander(date, choix = "score") {
    console.log("graph");

    fetch("http://127.0.0.1:5000/show_grahique/", {
        method: "POST",
        body: JSON.stringify({ date, choix }),
        headers: {
            "content-type": "application/json",

        },
    })
    // .then(response => response.text())  // Utiliser text() d'abord pour voir les données brutes
    // .then(value => console.log(value))  // Ensuite, les convertir en JSON
    // .catch(e => { console.log(e); })



}