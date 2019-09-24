import React from 'react';
import { post } from './utilities';

export default class LoginForm extends React.Component{
login(){
        var username=document.getElementsByName("username")[0].value;
        var password=document.getElementsByName("password")[0].value;
        post(
            '/login/', 
            {'Content-Type' : 'application/json'}, 
            {username, password}
        )
        .then(console.log)
        .catch(console.log)
    }

    render(){
        return(<div id="login">
    <label >Username:</label>
    <input type="text" name="username" /> 
    <label>Password:</label>
    <input type="password" name="password" />
    <button onClick={this.login} type="submit" value="Login">login</button>
    </div>
        );
    }
}