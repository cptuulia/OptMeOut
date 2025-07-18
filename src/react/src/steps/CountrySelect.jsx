/**
 * 
 * Section CountrySelect
 * 
 */
import PropTypes from 'prop-types';


import './steps_{{LANGUAGE_CODE}}.scss'
import './CountrySelect_{{LANGUAGE_CODE}}.scss'


function CountrySelect(props) {

    let countries = [
        "Austria",
        "Belgium (NL)",
        "Belgium (FR)",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czechia",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Ireland",
        "Italy",
        "Latvia",
        "Lithuania",
        "Luxembourg",
        "Maltha",
        "Netherlands",
        "Poland",
        "Portugal",
        "Romania",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden"
    ];


    //
    // Change country
    //
    const changeCountry = (country, e) => {
        props.emitUpdateFormdata("country", country);
        props.emitChangeSection("closeSection");
    };

    return (
        <div className="step" id="countrySelect">
            <h1>[[splash.countries.h1]]</h1> 
            <div
                className='closeButton'
                onClick={(e) => props.emitChangeSection("closeSection", e)}
            >
                &nbsp;
            </div>

            {/* left column*/}
            <div className="navigation">
                <ul className='leftColumn'>
                    {
                        countries.map((country, index) => {
                            if (index <= countries.length / 2) {
                                return (
                                    <li
                                        className="intro"
                                        key={"country" + index}
                                        onClick={(e) => changeCountry(country)}
                                    >
                                        {country}
                                    </li>)
                            } else {
                                return (<></>)
                            }

                        })
                    }
                </ul>

                {/* right column*/}
                <ul className='rightColumn'>
                    {
                        countries.map((country, index) => {
                            if (index >= countries.length / 2) {
                                return (
                                    <li
                                        className="intro"
                                        key={"country" + index}
                                        onClick={(e) => changeCountry(country)}
                                    >
                                        {country}
                                    </li>)
                            } else {
                                return (<></>)
                            }
                        })
                    }
                </ul>

            </div>
        </div>

    )
}


CountrySelect.propTypes = {
    emitChangeSection: PropTypes.func,
    emitUpdateFormdata: PropTypes.func, 
};
export default CountrySelect