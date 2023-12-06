

import './App.scss'
import Routes from './Routes'
import Header from './components/Header/Header'


import { DataProvider } from './contexts/DataContext'



function App() {


  return (
    <>
      <DataProvider >
        <Header />
        <Routes />
      </DataProvider>

    </>
  )
}

export default App
