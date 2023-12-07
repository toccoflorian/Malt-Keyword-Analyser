import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { SendNewJour } from "../../functions/dataFunctions"

export default function AddNewJour() {

    const navigate = useNavigate();
    const [html, setHtml] = useState(null)

    function handleSubmit(e) {
        e.preventDefault();
        try {
            html &&
                SendNewJour(html);
            navigate("/")
        } catch {
            null;
        }
    }

    return (<>
        <div>
            <h1>Ajout d&#39;un nouveau jour</h1>

            <form onSubmit={handleSubmit}>

                <textarea onChange={(e) => setHtml(e.target.value)}
                    name="newJourHTML"
                    id="" cols="100"
                    rows="30"
                    placeholder="Coller l'élèment HTML ici">
                </textarea>

                <div className={`d-flex justify-space-e`}>

                    <button type="submit">Valider</button>
                    <button onClick={() => navigate("/")}>Annuler</button>
                </div>

            </form>

        </div>
    </>)
}