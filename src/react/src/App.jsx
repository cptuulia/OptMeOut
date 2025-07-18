import { useState } from 'react'


import './style/App_{{LANGUAGE_CODE}}.scss'
import Header from "./components/Header/Header_{{LANGUAGE_CODE}}.jsx";

import About from "./steps/About_{{LANGUAGE_CODE}}.jsx";
import Step1 from "./steps/Step1_{{LANGUAGE_CODE}}.jsx";
import Step2 from "./steps/Step2_{{LANGUAGE_CODE}}.jsx";
function App() {
  const [currentSection, setCurrentSection] = useState("step2")
  let currentStep = "step1"


  //
  // Change visible section
  //
  const changeSection = (section, e) => {

    if (section.startsWith("step")) {
      currentStep = section
    }
    if (section == "closeSection") {
      section == currentStep
    }

    setCurrentSection(section);
  }

  return (
    <>

      <header>
        <Header
          emitChangeSection={changeSection}
        />
      </header>


      <div id="mainContent">

        {/* Step 1 Introduction*/}
        {currentSection == "step1" &&
          <Step1
            emitChangeSection={changeSection}
          />
        }

        {/* Step 2 splash  */}
        {currentSection == "step2" &&
          <Step2
            emitChangeSection={changeSection}
          />
        }

        {/* About section */}
        {currentSection == "about" &&
          <About
            emitChangeSection={changeSection}
          />
        }

      </div>
    </>
  )
}

export default App
