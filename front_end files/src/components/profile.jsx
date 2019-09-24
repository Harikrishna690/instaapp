import React from 'react';
import { get, getStatic, getUrl } from './utilities';

export default class profile extends React.Component{
    constructor(props){
        super(props);
        this.state={};
    }
    async UNSAFE_componentWillMount(){
        const that = this;
        await get(
           '/data/user/get',
           {'Content-Type':'application/json'}
        )
        .then(res => res.json())
        .then(data => {
            that.setState(data);
            // console.log(this.state["Image"]);
            const k= getUrl(this.state["Image"])
            console.log(k);
        })
        .catch(console.log)
    }
    render(){
        return(
            //   <div>username is{typeof this.state["Image"]} </div>
            <div className="container">
                <div className="card">
                    <div className="media">
                        <div className="media-left">
                            {typeof this.state["Image"]}
                            <figure className="image is-48x48">
                                <img    
                                src={this.state["Image"]}
                                alt="profile"/> 
                                
                            </figure>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}