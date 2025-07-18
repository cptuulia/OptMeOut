import {useState } from 'react'


import './style/App_[[LANGUAGE_CODE]].scss'
import Header from "./components/Header/Header_[[LANGUAGE_CODE]].jsx";

import About from "./steps/About_[[LANGUAGE_CODE]].jsx";
import Step1 from "./steps/Step1_[[LANGUAGE_CODE]].jsx";
import Step2 from "./steps/Step2_[[LANGUAGE_CODE]].jsx";
import CountrySelect from "./steps/CountrySelect_[[LANGUAGE_CODE]].jsx";


function App() {
  const [currentSection, setCurrentSection] = useState("step2")
  const [currentStep, setCurrentStep] = useState("step2")
  const [formData, setFormData] = useState({ country: ''})
  

  //
  // Change visible section
  //
  const changeSection = (section, e) => {

    if (section.startsWith("step")) {
      setCurrentStep(section);
    }
    if (section == "closeSection") {
      section  = currentStep;
    }
    setCurrentSection(section);
  }

  //
  // update form data
  //
  const updateFormdata = (field, value, e) => {
    let x = formData;
    x[field] =value
    setFormData(x)
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

        {/* Select Country */}
        {currentSection == "selectCountry" &&
          <CountrySelect
            emitChangeSection={changeSection}
            emitUpdateFormdata={updateFormdata}
           
          />
        }
        {/* About section */}
        {currentSection == "about" &&
          <About
            emitChangeSection={changeSection}
          />
        }
      </div>



      
    {/* ==============   Debug data ================ */}
     <div style={{ "clear": "both"}}> </div>
      <pre>
        section: {currentSection} current step: {currentStep} FormData:  Country: {formData.country}
      </pre>
    </>
  )
}

export default App
