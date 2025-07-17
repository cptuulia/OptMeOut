import { useState } from 'react'


import './style/App_{{LANGUAGE_CODE}}.scss'
import Header from "./components/Header/Header_{{LANGUAGE_CODE}}.jsx";
import Step1 from "./steps/Step1_{{LANGUAGE_CODE}}.jsx";
function App() {
  const [currentStep, setCurrentStep] = useState(1)

  //
  // Change Step
  //
  const changeStep = (stepNUmber, e) => {
    setCurrentStep(stepNUmber);
  };


  return (
    <>

      <header> <Header /></header>


      <div id="mainContent">
        {currentStep == 1 &&
          <Step1
            emitChangeStep={changeStep}
          />}

        {currentStep == 2 &&
          <div>Step2</div>
        }
      </div>
    </>
  )
}

export default App
