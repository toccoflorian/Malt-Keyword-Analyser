

import './App.scss'
import Content from './components/Content/Content'
import Header from './components/Header/Header'

import { DataProvider } from './contexts/DataContext'


function App() {


  return (
    <>
      <DataProvider >
        <Header />
        <Content />
      </DataProvider>

    </>
  )
}

export default App
