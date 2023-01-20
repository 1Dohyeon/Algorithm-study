import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';  // .이라는 기호는 현재 디렉토리를 의미함. 즉 현재 디렉토리의 App.js를 의미
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App /> 
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
