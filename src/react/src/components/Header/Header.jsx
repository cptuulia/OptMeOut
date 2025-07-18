/**
 * 
 * Component to render the header
 * 
 */
import PropTypes from 'prop-types';
import { useState } from 'react';

import '/src/components/Header/Header_[[LANGUAGE_CODE]].scss'
import LanguageSelect from "/src/components/LanguageSelect/LanguageSelect_[[LANGUAGE_CODE]].jsx";

function Header(props) {
        return (
                <>
                        <div id="headerLanguageSelect" >
                                <LanguageSelect />
                        </div>
                        <div
                                id="headerAbout"
                                onClick={(e) => props.emitChangeSection("about", e)}
                        >
                                [[menu.about]]
                        </div>
                </>

        )
}

Header.propTypes = {
        emitChangeSection: PropTypes.func,  // Change step
};
export default Header