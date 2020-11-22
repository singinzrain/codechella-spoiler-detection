import React from 'react';
import {MainRouter} from './MainRouter.js';
import {BrowserRouter} from 'react-router-dom';


const App = () => (
  <BrowserRouter>
  <MainRouter />
  </BrowserRouter>
);

export default App;
