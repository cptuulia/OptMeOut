/**
 * 
 * Component to render the header
 * 
 */

import '/src/components/Header/Header_{{LANGUAGE_CODE}}.scss'
import LanguageSelect from "/src/components/LanguageSelect/LanguageSelect_{{LANGUAGE_CODE}}.jsx";

function Header() {
        return (
                <>
                        <div id="headerLanguageSelect" >
                                <LanguageSelect />
                        </div>
                        <div id="headerAbout">
                                About
                        </div>
                </>

        )
}

export default Header