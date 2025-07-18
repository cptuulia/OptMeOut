import { useState } from 'react'


import './style/App_{{LANGUAGE_CODE}}.scss'
import Header from "./components/Header/Header_{{LANGUAGE_CODE}}.jsx";

import Step1 from "./steps/About_{{LANGUAGE_CODE}}.jsx";
import Step1 from "./steps/Step1_{{LANGUAGE_CODE}}.jsx";
function App() {
  const [currentSection, setCurrentSection] = useState("step1")
  let currentStep = "step1"
  

  //
  // Change visible section
  //
  const changeSection = (section, e) => {

    if (section.startsWith("step")) {
      currentStep = section
    }
    
    setCurrentSection(section);
  };

  return (
    <>

      <header>
        <Header
          emitChangeSection={changeSection}
        />
      </header>


      <div id="mainContent">
        {currentSection == "step1" &&
          <Step1
            emitChangeSection={changeSection}
          />}

        {currentSection == "step2" &&
          <div>Step2</div>
        }

         {currentSection == "about" &&
          <About
            emitChangeSection={changeSection}
          />}
        }
      </div>
    </>
  )
}

export default App
