import Jours from "../../components/Jours/Jours";
import { Link } from "react-router-dom"

export default function Home() {

    // function handleClick() {
    //     return <Link to={"/AddNewJour"}> edzedz</Link >
    // }

    return (<>
        <div className="widthfull ptr25">
            <Link to={`AddNewJour`}>Ajouter un jour</Link>
            <Jours />
        </div>
    </>)
}

