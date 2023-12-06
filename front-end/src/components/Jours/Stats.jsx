import { useState } from "react"
import styles from "./Stats.module.scss";

export default function Stats({ ...stats }) {

    const [listOfWord, setListOfWord] = useState([]);

    const bests = stats.stats


    function sortWord(categorie) {
        const words = bests[categorie]
        let key = categorie.split("_")[1]
        key === "apparition" &&
            (key = "nombre_" + key);
        categorie === "top_position" ?
            words.sort((a, b) => parseFloat(a[key]) - parseFloat(b[key]))
            :
            words.sort((a, b) => parseFloat(b[key]) - parseFloat(a[key]))
        return (<>
            {words.map(word => {

                return (<>
                    <li className={`d-flex justify-space-b align-center `}>
                        <p className={`widthmin`}>{word.keyword}:</p>
                        <p>{word[key]}</p>

                    </li>
                </>)
            })}
        </>)
    }

    return (<>
        {Object.keys(bests).map(categorie => {

            return (<>
                <div className={`prl10`}>
                    <h4>Meilleures {categorie.split("_")[1]}s</h4>
                    <ul className={`mrl10`}>
                        {sortWord(categorie)}
                    </ul>
                </div>
            </>)
        })}
    </>)
}