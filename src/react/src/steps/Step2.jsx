/**
 * 
 * Step2
 * 
 * splash
 * 
 */
import PropTypes from 'prop-types';


import './steps.scss'
import './Step2.scss'


function Step2(props) {

        return (
                <div className="step" id="Step2">
                        <h1>[[page.fallback.header]]</h1>
                        <p1>[[page.fallback.intro]]</p1>
                        <div className='clearBoth'></div>

                        {/* Buttons */}
                        <div className='buttonsRow'>
                                <div
                                        className="buttonDefault"
                                        onClick={(e) => props.emitChangeSection("about", e)}
                                >
                                        [[menu.about]]
                                </div>
                                <div 
                                        className="buttonDefault"
                                        onClick={(e) => props.emitChangeSection("selectCountry", e)}
                                >
                                        [[page.fallback.button]]
                                </div>
                        </div>

                </div>

        )
}


Step2.propTypes = {
        emitChangeSection: PropTypes.func,  // Change step
};

export default Step2