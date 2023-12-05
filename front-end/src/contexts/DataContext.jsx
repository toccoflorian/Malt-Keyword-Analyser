import { createContext, useEffect, useState } from "react"

export const DataContext = createContext()



export function DataProvider({ children = null }) {
    const [data, setData] = useState(null)


    useEffect(() => {
        fetch("http://127.0.0.1:5000/get_jours/", {
            method: "GET",
        })
            .then(response => response.json())  // Utiliser text() d'abord pour voir les données brutes
            .then(value => {
                console.log(value);
                setData(value)
            })  // Ensuite, les convertir en JSON
            .catch(e => { console.log(e); })
    }, [])



    return (<>
        <DataContext.Provider value={{ ...data }}>
            {children}
        </DataContext.Provider>
    </>)
}


// function GraphCommander() {

//     useEffect(() => {
//         fetch("http://127.0.0.1:5000/show_grahique/", {
//             method: "POST",
//             body: JSON.stringify({ date: "02-12-2023", choix: "score" }),
//             headers: {
//                 "content-type": "application/json",

//             },
//         })
//             .then(response => response.text())  // Utiliser text() d'abord pour voir les données brutes
//             .then(value => console.log(value))  // Ensuite, les convertir en JSON
//             .catch(e => { console.log(e); })
//     }, [])


// }