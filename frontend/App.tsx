// frontend/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AuthPage from './pages/auth';
import StatisticsPage from './pages/StatisticsPage';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={AuthPage} />
        <Route path="/statistics" component={StatisticsPage} />
      </Switch>
    </Router>
  );
};

export default App;