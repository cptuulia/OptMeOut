import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index_{{LANGUAGE_CODE}}.css'
import App from './App_{{LANGUAGE_CODE}}.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
