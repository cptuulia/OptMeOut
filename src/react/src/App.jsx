import { useState } from 'react'
import './style/App_{{LANGUAGE_CODE}}.scss'


import Header from "./components/Header/Header_{{LANGUAGE_CODE}}.jsx";
import Step1 from "./steps/Step1_{{LANGUAGE_CODE}}.jsx";
function App() {
  const [currentStep] = useState(1)

  return (
    <>

      <header> <Header /></header>
      <div id="mainContent">
        { currentStep == 1 && <Step1 />}
      </div>
    </>
  )
}

export default App
