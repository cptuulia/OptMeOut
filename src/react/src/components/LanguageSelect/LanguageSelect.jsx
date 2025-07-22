/**
 * 
 * Component to render the language select
 * 
 */


function LanguageSelect() {
       const handleChange = (e) => {
                let url = '/' + e.target.value 
                window.location.href = url
        };

        return (
                <>
                        <select  onChange={handleChange}>
                        [[LANGUAGE_HTML_OPTIONS]]
                        </select>
                </>

        )
}

export default LanguageSelect