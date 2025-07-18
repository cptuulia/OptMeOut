/**
 * 
 * Section About
 * 
 */
import PropTypes from 'prop-types';


import './steps_{{LANGUAGE_CODE}}.scss'
import './About_{{LANGUAGE_CODE}}.scss'


function About(props) {


        return (
                <div className="step" id="About">
                      <h1>[[about.h1]]</h1>
                      <p>[[about.p]]</p>
                </div>

        )
}


About.propTypes = {
        emitChangeSection: PropTypes.func,  // Change step
};
export default About