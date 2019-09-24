import React from 'react';
import ReactDOM from 'react-dom';
import Home from './components/home'
import LoginForm from './components/login';
import profile from './components/profile';
import profiledata from './components/profiledata';
import { Route,  BrowserRouter as Router } from 'react-router-dom';

const routing = (
    <Router>
        <Route exact path="/home" component={Home} />
        <Route path="/lon" component={LoginForm} />
        <Route path="/profile" component={profile}/>  
        <Route path="/profiledata" component={profiledata}/>  
    </Router>
  )


ReactDOM.render(routing, document.getElementById('root'));
