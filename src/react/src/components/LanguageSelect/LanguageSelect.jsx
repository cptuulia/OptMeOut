/**
 * 
 * Component to render the language select
 * 
 */


function LanguageSelect() {
       const handleChange = (e) => {
                let url = 'index_' + e.target.value +'.html'
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