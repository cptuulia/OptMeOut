import { useState } from 'react'
import './style/App_{{LANGUAGE_CODE}}.scss'


import Header from "./components/Header/Header_{{LANGUAGE_CODE}}.jsx";
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <header> <Header /></header>

    </>
  )
}

export default App
