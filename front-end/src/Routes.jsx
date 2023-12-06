

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home/Home";
import AddNewJour from "./pages/AddNewJour/AddNewJour";

export default function AppRoutes() {

    return (<>
        <Router>
            <Routes>
                <Route exact path="/" Component={Home} />
                <Route path="/AddNewJour" Component={AddNewJour} />
            </Routes>
        </Router>
    </>)
}