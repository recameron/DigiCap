import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app.jsx'; // ← This is where your main UI comes from
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App /> {/* This is what you see in the browser */}
  </React.StrictMode>
);
