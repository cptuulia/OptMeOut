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
                        <div 
                                className='closeButton'
                                onClick={(e) => props.emitChangeSection("step2", e)}
                        >
                                &nbsp;
                        </div>
                      <h1>[[page.about.title]]</h1>
                      <h1 className='intro'>[[page.about.h1]]</h1>
                      <p>[[page.about.p1]]</p>
                      <p>[[page.about.p2]]</p>
                      <h1  className='intro'>[[page.about.h2]]</h1>
                      <p>[[page.about.p3]]</p>
                      <p>[[page.about.p4]]</p>
                </div>

        )
}


About.propTypes = {
        emitChangeSection: PropTypes.func,  // Change step
};
export default About