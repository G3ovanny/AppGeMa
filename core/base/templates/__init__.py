{% load render_vite_bundle %}
<!DOCTYPE html>
<html lang="es">
    
<head>
  
    <meta charset="UTF-8" /> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Talento Humano Upec</title>
  </head>
  
  <body>
  
    <div id="root"></div>
  
    {% if debug %}
    <script type="module" src=" http://localhost:5173/@vite/client"></script>
    <!-- If you're using vite with React, this next script will be needed for HMR -->
    <script type="module">
      import RefreshRuntime from ' http://localhost:5173/@react-refresh'
      if (RefreshRuntime) {
        RefreshRuntime.injectIntoGlobalHook(window)
        window.$RefreshReg$ = () => { }
        window.$RefreshSig$ = () => (type) => type
        window.__vite_plugin_react_preamble_installed__ = true
      }
    </script>
    
    <script type="module" src=" http://localhost:5173/main.jsx"></script>
    {% else %}
  {% comment %} <script type="module" src=" http://localhost:5173/@vite/client"></script>
    <!-- If you're using vite with React, this next script will be needed for HMR -->
    <script type="module">
      import RefreshRuntime from ' http://localhost:5173/@react-refresh'
      if (RefreshRuntime) {
        RefreshRuntime.injectIntoGlobalHook(window)
        window.$RefreshReg$ = () => { }
        window.$RefreshSig$ = () => (type) => type
        window.__vite_plugin_react_preamble_installed__ = true
      }
    </script>
    <script type="module" src=" http://localhost:5173/main.jsx"></script> {% endcomment %}
  
    {% render_vite_bundle %} 
    {% endif %}
  </body>
  
  </html>