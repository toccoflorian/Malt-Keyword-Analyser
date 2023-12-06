import { useNavigate } from "react-router-dom"

export default function AddNewJour() {

    const navigate = useNavigate();

    return (<>
        <div>
            <h1>Ajout d&#39;un nouveau jour</h1>
            <textarea name="" id="" cols="100" rows="30" placeholder="Coller l'élèment HTML ici"></textarea>
            <div className={`d-flex justify-space-e`}>
                <button>Valider</button>
                <button onClick={() => navigate("/")}>Annuler</button>
            </div>
        </div>
    </>)
}