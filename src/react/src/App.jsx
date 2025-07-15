import { useState } from 'react'
import './App_{{LANGUAGE_CODE}}.css'

import LanguageSelect from "./components/LanguageSelect/LanguageSelect_{{LANGUAGE_CODE}}.jsx";
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      TEST
       <LanguageSelect/>
    </>
  )
}

export default App
