import { useContext, useState } from "react";
import { DataContext } from "../../contexts/DataContext";
import { GraphCommander } from "../../functions/dataFunctions";
import Stats from "./Stats";
import styles from "./Jours.module.scss";

export default function Jours() {

    const [jours, setJours] = useState([]);

    const data = useContext(DataContext);
    if (jours !== data) {
        setJours(data)
    }

    // afficher les graphiques
    function handleClickGraph(e) {
        GraphCommander(e.target.id, e.target.name)
    }

    return (<>
        <ul className={`d-flex flex-wrap justify-space-e `}>

            {/* map sur la liste d'objets */}
            {Object.keys(jours).map((key, index) => {
                const bests = jours[key].bests
                const jourFiches = jours[key].fiches;
                return (
                    <li key={key + index} className={`${styles.cards} prl10`}>
                        <h3>{key}</h3>
                        <p>Nombre d&#39;apparitions: {jourFiches.reduce((acc, value) => acc + parseInt(value.nombre_apparition), 0)}</p>
                        <p>Nombre de keywords: {jourFiches.length}</p>

                        <div className={`d-flex fs10`}>
                            <Stats stats={bests} />
                        </div>

                        <div className={`d-flex`}>
                            <button onClick={handleClickGraph} id={key} name="position" className={`widthmin`}>Graph positions</button>
                            <button onClick={handleClickGraph} id={key} name="nombre_apparition" className={`widthmin`}>Graph nombres d&#39;apparitions</button>
                            <button onClick={handleClickGraph} id={key} name="score" className={`widthmin`}>Graph scores</button>
                        </div>
                    </li>
                )
            })}
        </ul>
    </>)
}