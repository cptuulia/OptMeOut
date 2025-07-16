/**
 * 
 * Step 1
 * 
 */

import './steps_{{LANGUAGE_CODE}}.scss'
function Step1() {

        return (
                <div id="step">
                        <h1>[[step1.title]]</h1>
                        <p class="intro">
                                [[step1.intro]]
                        </p>
                        <div id="step1Buttons">
                                <div class="tellMeMore">[[button.tellmemore]]</div>
                                <div class="buttonActive">[[button.OptMeOut]]</div>
                        </div>
                </div>

        )
}

export default Step1